#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
from typing import Any, cast, TypeVar, Callable, Iterable, Union
import subprocess


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
            os.rename(os.path.join(os.environ['HOME'], '.local', path), os.path.join(os.environ['HOME'], '.local', 'git-filter-repo'))

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
    os.rename('/tmp/lazygit', os.path.join(local_bin_dir, 'lazygit'))

def install_excelchop():
    asset = get_github_asset('mitchpaulus', 'excelchop', lambda a: a.name.startswith('linux-x64-framework-dependent'))
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

    # Extract the 'excelchop' executable from the tar.xz archive
    print(f'Extracting {asset.name} archive...', file=sys.stderr)
    completed_process = subprocess.run(['tar', '-xf', tar_xz_path, 'excelchop'], cwd='/tmp/')
    if completed_process.returncode != 0:
        print(f'Error extracting {asset.name} archive', file=sys.stderr)
        sys.exit(1)

    # Remove the tar.xz archive
    print(f"Removing '{asset.name}' archive...", file=sys.stderr)
    os.remove(tar_xz_path)

    # Move '/tmp/lazygit' to LOCALBIN, overwriting if necessary
    print(f"Moving lazygit to {local_bin_dir}", file=sys.stderr)
    os.rename('/tmp/excelchop', os.path.join(local_bin_dir, 'excelchop'))


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

if __name__ == "__main__":
    local_bin_dir = os.environ.get('LOCALBIN')
    if local_bin_dir is None:
        print('LOCALBIN environment variable not set.', file=sys.stderr)
        sys.exit(1)

    local_bin_dir = cast(str, local_bin_dir)

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
    }

    help_lines = [
        'Usage: install.py [program]',
        '',
        'Available programs:',
    ]
    for program_name in programs:
        help_lines.append(f'  {program_name}')

    while (idx < len(sys.argv)):
        if (sys.argv[idx] == "-h" or sys.argv[idx] == "--help"):
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
