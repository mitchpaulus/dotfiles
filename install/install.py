#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
from typing import Any, cast
import subprocess


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


if __name__ == "__main__":
    local_bin_dir = os.environ.get('LOCALBIN')
    if local_bin_dir is None:
        print('LOCALBIN environment variable not set.', file=sys.stderr)
        sys.exit(1)

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

    while (idx < len(sys.argv)):
        if (sys.argv[idx] == "-h"):
            print("""
            Usage:
                install.py [options] [program]
            Options:
                -h, --help: Show this help message and exit.
            """)
            sys.exit(0)
        else:
            program = sys.argv[idx]
        idx += 1

    if program == "git-filter-repo":
        install_git_filter_repo()
    elif program == "json-tui":
        install_json_tui(local_dir)
    else:
        print(f"Error: Unknown program '{program}'", file=sys.stderr)
        sys.exit(1)

