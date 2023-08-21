#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
from typing import Any, cast, TypeVar, Callable, Iterable, Union, Optional
import subprocess
import shutil


T1 = TypeVar('T1')
def first(iterable: Iterable[T1], predicate: Callable[[T1], bool]) -> Union[T1, None]:
    """
    Return the first element in the given iterable that matches the given predicate, or None if no element matches.
    """
    for x in iterable:
        if predicate(x):
            return x
    return None

class GitHubAsset:
    def __init__(self, asset: Any):
        self.id = asset['id']
        self.name = asset['name']
        self.browser_download_url = asset['browser_download_url']

class GitHubReleaseResponse:
    def __init__(self, data: Any):
        self.assets = list(map(GitHubAsset, data['assets']))

def localbin_defined() -> bool:
    # Check that LOCALBIN environment variable is set
    return os.environ.get('LOCALBIN') is not None

def latest_github_release(username: str, repo: str) -> GitHubReleaseResponse:
    """
    Get the latest release from GitHub.
    """
    url = f'https://api.github.com/repos/{username}/{repo}/releases/latest'
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Error: {response.status_code}', file=sys.stderr)
        sys.exit(1)
    try:
        decoded_json = response.json()
        return GitHubReleaseResponse(decoded_json)
    except requests.exceptions.JSONDecodeError:
        print('Error: Unable to parse JSON from GitHub releases', file=sys.stderr)
        sys.exit(1)

def get_github_asset(username: str, repo: str, predicate: Callable[[GitHubAsset], bool]) -> GitHubAsset:
    # Get latest release from GitHub
    latest_release = latest_github_release(username, repo)

    # Find first asset matching regex 'git-filter-repo-.*.tar.xz'
    asset = next((a for a in latest_release.assets if predicate(a)), None)

    if asset is None:
        print(f'Error: Unable to find {username}/{repo} asset matching predicate', file=sys.stderr)
        sys.exit(1)

    asset = cast(GitHubAsset, asset)
    return asset


def install_deb(username: str, repo: str, predicate: Callable[[GitHubAsset], bool]):
    asset = get_github_asset(username, repo, predicate)
    # Download asset to /tmp
    print(f"Downloading '{asset.name}' to /tmp", file=sys.stderr)
    response = requests.get(asset.browser_download_url)

    if response.status_code != 200:
        print(f'Error downloading {asset.browser_download_url}: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    with open('/tmp/' + asset.name, 'wb') as f:
        f.write(response.content)

    # Install the downloaded .deb file
    print(f'Installing {asset.name}', file=sys.stderr)
    completed_process = subprocess.run(['sudo', 'dpkg', '-i', '/tmp/' + asset.name])

    if completed_process.returncode != 0:
        print(f'Error installing {asset.name}', file=sys.stderr)
        sys.exit(1)


def install_git_filter_repo():
    if not localbin_defined():
        print('LOCALBIN environment variable not set.', file=sys.stderr)
        sys.exit(1)

    local_bin_dir = os.environ['LOCALBIN']

    # Make '~/.local' directory if it doesn't exist
    local_dir = os.environ['HOME'] + '/.local'
    if not os.path.isdir(local_dir):
        os.mkdir(local_dir)

    # Get latest release from GitHub
    latest_release = latest_github_release('newren', 'git-filter-repo')

    # Find first asset matching regex 'git-filter-repo-.*.tar.xz'
    asset = next((a for a in latest_release.assets if a.name.startswith('git-filter-repo-')), None)

    if asset is None:
        print('Error: Unable to find git-filter-repo asset', file=sys.stderr)
        sys.exit(1)

    asset = cast(GitHubAsset, asset)

    # Download asset
    print(f'Downloading {asset.name}...', file=sys.stderr)
    response = requests.get(asset.browser_download_url)
    if response.status_code != 200:
        print(f'Error downloading {asset.browser_download_url}: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    # Remove any existing directory starting with 'git-filter-repo' in ~/.local
    for path in os.listdir(os.path.join(os.environ['HOME'], '.local')):
        if path.startswith('git-filter-repo'):
            full_path = os.path.join(os.environ['HOME'], '.local', path)
            print(f"Removing existing git-filter-repo directory: '{full_path}'", file=sys.stderr)
            subprocess.run(['rm', '-rf', full_path])

    # Extract asset
    tar_xz_path = os.path.join(os.environ['HOME'], '.local', asset.name)
    print(f"Saving '{tar_xz_path}'", file=sys.stderr)
    with open(tar_xz_path, 'wb') as f:
        f.write(response.content)

    # Extract the tar.xz archive
    print(f'Extracting {asset.name} archive...', file=sys.stderr)
    completed_process = subprocess.run(['tar', '-xJf', tar_xz_path], cwd=local_dir)
    if completed_process.returncode != 0:
        print(f'Error extracting {asset.name} archive', file=sys.stderr)
        sys.exit(1)

    # Rename the directory starting with 'git-filter-repo' to 'git-filter-repo'
    for path in os.listdir(os.path.join(os.environ['HOME'], '.local')):
        if path.startswith('git-filter-repo') and os.path.isdir(os.path.join(os.environ['HOME'], '.local', path)):
            new_path = os.path.join(os.environ["HOME"], ".local", "git-filter-repo")
            print(f"Renaming '{path}' to '{new_path}'...", file=sys.stderr)
            shutil.move(os.path.join(os.environ['HOME'], '.local', path), os.path.join(os.environ['HOME'], '.local', 'git-filter-repo'))

    # Remove the tar.xz archive
    print(f"Removing '{asset.name}' archive...", file=sys.stderr)
    os.remove(tar_xz_path)

    # Symlink git-filter-repo to LOCALBIN
    print(f"Symlinking git-filter-repo to '{local_bin_dir}'...", file=sys.stderr)

    # Remove existing symlink if it exists
    symlink_dest = local_bin_dir + '/git-filter-repo'
    if os.path.lexists(symlink_dest):
        os.remove(symlink_dest)

    os.symlink(os.path.join(os.environ['HOME'], '.local', 'git-filter-repo', 'git-filter-repo'), symlink_dest)


def install_json_tui(local_dir: str):
    latest_release = latest_github_release('ArthurSonzogni', 'json-tui')

    # Get assest matching regex 'json-tui-.*-Linux.sh'
    asset = next((a for a in latest_release.assets if a.name.startswith('json-tui-') and a.name.endswith('-Linux.sh')), None)

    if asset is None:
        print('Error: Unable to find json-tui-X.X.X-Linux.sh asset', file=sys.stderr)
        sys.exit(1)

    asset = cast(GitHubAsset, asset)

    # Download asset
    print(f'Downloading {asset.name}...', file=sys.stderr)
    response = requests.get(asset.browser_download_url)

    if response.status_code != 200:
        print(f'Error downloading {asset.browser_download_url}: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    # Download file to /tmp, overwriting any existing file. Make sure the file is executable.
    print(f'Saving {asset.name} to /tmp/{asset.name}', file=sys.stderr)

    with open('/tmp/' + asset.name, 'wb') as f:
        f.write(response.content)

    os.chmod('/tmp/' + asset.name, 0o755)

    # Run the downloaded script, with arguments --prefix=<LOCALBIN> and --include-subdir
    print(f'Running {asset.name}', file=sys.stderr)
    completed_process = subprocess.run(['/tmp/' + asset.name, '--prefix=' + local_dir, '--include-subdir'])

    if completed_process.returncode != 0:
        print(f'Error running {asset.name}', file=sys.stderr)
        sys.exit(1)

def install_lazygit():
    local_bin_dir = cast(str, os.environ.get('LOCALBIN'))
    asset = get_github_asset('jesseduffield', 'lazygit', lambda a: a.name.startswith('lazygit') and a.name.endswith('Linux_x86_64.tar.gz'))

    # Download asset
    print(f'Downloading {asset.name}...', file=sys.stderr)
    response = requests.get(asset.browser_download_url)

    if response.status_code != 200:
        print(f'Error downloading {asset.browser_download_url}: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    # Save asset
    tar_xz_path = os.path.join('/tmp/', asset.name)
    print(f"Saving '{tar_xz_path}'", file=sys.stderr)
    with open(tar_xz_path, 'wb') as f:
        f.write(response.content)

    # Extract the 'lazygit' executable from the tar.xz archive
    print(f'Extracting {asset.name} archive...', file=sys.stderr)
    completed_process = subprocess.run(['tar', '-xf', tar_xz_path, 'lazygit'], cwd='/tmp/')
    if completed_process.returncode != 0:
        print(f'Error extracting {asset.name} archive', file=sys.stderr)
        sys.exit(1)

    # Remove the tar.xz archive
    print(f"Removing '{asset.name}' archive...", file=sys.stderr)
    os.remove(tar_xz_path)

    # Move '/tmp/lazygit' to LOCALBIN, overwriting if necessary
    print(f"Moving lazygit to {local_bin_dir}", file=sys.stderr)
    shutil.move('/tmp/lazygit', os.path.join(local_bin_dir, 'lazygit'))

def install_excelchop():
    asset = get_github_asset('mitchpaulus', 'excelchop', lambda a: 'linux-x64' in a.name and 'framework-dependent' in a.name)
    print(f'Downloading {asset.name}...', file=sys.stderr)
    response = requests.get(asset.browser_download_url)

    if response.status_code != 200:
        print(f'Error downloading {asset.browser_download_url}: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    # Save asset
    zip_path = os.path.join('/tmp/', asset.name)
    print(f"Saving '{zip_path}'", file=sys.stderr)
    with open(zip_path, 'wb') as f:
        f.write(response.content)

    # Extract the 'excelchop' executable from the tar.xz archive
    print(f'Extracting {asset.name} archive...', file=sys.stderr)
    completed_process = subprocess.run(['unzip', zip_path], cwd='/tmp/')
    if completed_process.returncode != 0:
        print(f'Error extracting {asset.name} archive', file=sys.stderr)
        sys.exit(1)

    # Remove the zip
    print(f"Removing '{asset.name}' archive...", file=sys.stderr)
    os.remove(zip_path)

    # Move '/tmp/excelchop' to LOCALBIN, overwriting if necessary
    print(f"Moving excelchop to {local_bin_dir}", file=sys.stderr)
    shutil.move('/tmp/excelchop', os.path.join(local_bin_dir, 'excelchop'))


def install_neovim():
    asset = get_github_asset('neovim', 'neovim', lambda a: a.name == 'nvim.appimage')
    print(f'Downloading {asset.name}...', file=sys.stderr)
    response = requests.get(asset.browser_download_url)

    if response.status_code != 200:
        print(f'Error downloading {asset.browser_download_url}: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    # Save asset to $HOME/apps. Create directory if necessary.
    app_dir = os.path.join(os.environ['HOME'], 'apps')
    if not os.path.exists(app_dir):
        os.mkdir(app_dir)

    app_path = os.path.join(app_dir, asset.name)
    print(f"Saving '{app_path}'", file=sys.stderr)
    with open(app_path, 'wb') as f:
        f.write(response.content)

    # Make the app executable
    os.chmod(app_path, 0o755)

    # Symlink to $LOCALBIN if it doesn't exist
    local_bin_dir = cast(str, os.environ.get('LOCALBIN'))
    print(f"Symlinking '{app_path}' to '{local_bin_dir}'", file=sys.stderr)
    if not os.path.exists(os.path.join(local_bin_dir, 'nvim')):
        os.symlink(app_path, os.path.join(local_bin_dir, 'nvim'))

def install_tabula_cli():
    asset = get_github_asset('tabulapdf', 'tabula-java', lambda a: a.name.endswith('.jar'))
    print(f'Downloading {asset.name}...', file=sys.stderr)
    response = requests.get(asset.browser_download_url)

    if response.status_code != 200:
        print(f'Error downloading {asset.browser_download_url}: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    # Save asset to $LOCALBIN.
    local_bin_dir = cast(str, os.environ.get('LOCALBIN'))
    jar_path = os.path.join(local_bin_dir, asset.name)
    print(f"Saving '{jar_path}'", file=sys.stderr)
    with open(jar_path, 'wb') as f:
        f.write(response.content)

def install_magcik():
    # Download file https://imagemagick.org/archive/binaries/magick to $LOCALBIN
    # Downloading the statically linked binary is so much simpler than dealing with outdated package managers
    local_bin_dir = cast(str, os.environ.get('LOCALBIN'))
    magick_path = os.path.join(local_bin_dir, 'magick')
    print(f"Saving '{magick_path}'", file=sys.stderr)
    response = requests.get('https://imagemagick.org/archive/binaries/magick')
    if response.status_code != 200:
        print(f'Error downloading https://imagemagick.org/archive/binaries/magick: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    with open(magick_path, 'wb') as f:
        f.write(response.content)

    # Make the file executable
    os.chmod(magick_path, 0o755)


def install_gh_cli():
    install_deb('cli', 'cli', lambda a: a.name.startswith('gh_') and a.name.endswith('_amd64.deb'))

def install_powershell():
    install_deb('PowerShell', 'PowerShell', lambda a: a.name.startswith('powershell') and a.name.endswith('_amd64.deb'))

def install_antlr():
    # Download from https://www.antlr.org/download/antlr-4.11.1-complete.jar
    # Save to /usr/local/lib, will have to run as root
    response = requests.get('https://www.antlr.org/download/antlr-4.11.1-complete.jar')
    if response.status_code != 200:
        print(f'Error downloading https://www.antlr.org/download/antlr-4.11.1-complete.jar: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    jar_path = '/usr/local/lib/antlr-4.11.1-complete.jar'
    print(f"Saving '{jar_path}'", file=sys.stderr)
    with open(jar_path, 'wb') as f:
        f.write(response.content)

def install_vivid():
    # Steps from README:
    # wget "https://github.com/sharkdp/vivid/releases/download/v0.8.0/vivid_0.8.0_amd64.deb"
    # sudo dpkg -i vivid_0.8.0_amd64.deb
    install_deb('sharkdp', 'vivid', lambda a: a.name.startswith('vivid') and a.name.endswith('_amd64.deb'))


def install_azcopy(local_bin_dir: str):
    # https://aka.ms/downloadazcopy-v10-linux
    # This is a tar.gz file
    # Contents:
    # azcopy_linux_amd64_10.19.0/
    # azcopy_linux_amd64_10.19.0/azcopy
    # azcopy_linux_amd64_10.19.0/NOTICE.txt

    response = requests.get('https://aka.ms/downloadazcopy-v10-linux')
    if response.status_code != 200:
        print(f'Error downloading https://aka.ms/downloadazcopy-v10-linux: {response.status_code}', file=sys.stderr)
        sys.exit(1)

    # Extract into directory in /tmp/, then move to $LOCALBIN
    with open('/tmp/azcopy.tar.gz', 'wb') as f:
        f.write(response.content)

    # List contents, get path to azcopy, using 'tar --list -f /tmp/azcopy.tar.gz'
    completed = subprocess.run(['tar', '--list', '-f', '/tmp/azcopy.tar.gz'], capture_output=True, encoding='utf-8')
    if completed.returncode != 0:
        print(f'Error listing contents of /tmp/azcopy.tar.gz: {completed.stderr}', file=sys.stderr)
        sys.exit(1)

    azcopy_path = None
    for line in completed.stdout.splitlines():
        if line.endswith('azcopy'):
            azcopy_path = line
            break

    if azcopy_path is None:
        print(f'Error finding azcopy in /tmp/azcopy.tar.gz', file=sys.stderr)
        sys.exit(1)

    # extract file
    print(f"Extracting '{azcopy_path}' from /tmp/azcopy.tar.gz", file=sys.stderr)
    completed = subprocess.run(['tar', '--extract', '-f', '/tmp/azcopy.tar.gz', azcopy_path], cwd='/tmp', capture_output=True, encoding='utf-8')

    # Move file
    azcopy_path = os.path.join('/tmp', azcopy_path)
    print(f"Moving '{azcopy_path}' to '{local_bin_dir}'", file=sys.stderr)
    shutil.move(azcopy_path, os.path.join(local_bin_dir, 'azcopy'))


if __name__ == "__main__":
    local_bin_dir_env: Optional[str] = os.environ.get('LOCALBIN')
    if local_bin_dir_env is None:
        print('LOCALBIN environment variable not set.', file=sys.stderr)
        sys.exit(1)

    local_bin_dir = cast(str, local_bin_dir_env)

    home_dir = os.environ.get('HOME')
    if home_dir is None:
        print('HOME environment variable not set.', file=sys.stderr)
        sys.exit(1)

    local_dir = os.path.join(home_dir, '.local')
    if not os.path.exists(local_dir):
        print(f'Creating {local_dir}', file=sys.stderr)
        os.mkdir(local_dir)

    idx = 1
    program = None

    programs = {
        "git-filter-repo": install_git_filter_repo,
        "json-tui": lambda: install_json_tui(local_dir),
        "lazygit": install_lazygit,
        "excelchop": install_excelchop,
        "neovim": install_neovim,
        "tabula-cli": install_tabula_cli,
        "magcik": install_magcik,
        "gh-cli": install_gh_cli,
        "powershell": install_powershell,
        "antlr": install_antlr,
        "vivid": install_vivid,
        "azcopy": lambda: install_azcopy(local_bin_dir),
    }

    while (idx < len(sys.argv)):
        if (sys.argv[idx] == "-h" or sys.argv[idx] == "--help"):
            help_lines = [ 'Usage: install.py [program]', '', 'Available programs:', ]
            for program_name in programs:
                help_lines.append(f'  {program_name}')
            print('\n'.join(help_lines), end='\n')
            sys.exit(0)
        else:
            program = sys.argv[idx]
        idx += 1


    if program is None:
        print('Error: No program specified.', file=sys.stderr)
        print('Possible programs:', file=sys.stderr)
        for program in programs:
            print(f' {program}', file=sys.stderr)
        sys.exit(1)

    program_func = programs.get(program)

    if program_func is None:
        print(f'Error: Unknown program "{program}"', file=sys.stderr)
        print(f'Possible programs:', file=sys.stderr)
        for program in programs:
            print(f' {program}', file=sys.stderr)
        sys.exit(1)

    program_func()
