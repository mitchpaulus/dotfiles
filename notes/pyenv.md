# `pyenv`

Builds Python versions.

For Ubuntu, need <https://github.com/pyenv/pyenv/wiki#suggested-build-environment>:

```
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Automatic installer: `curl https://pyenv.run | bash`

```
pyenv install 3.12 # Takes a while
pyenv global 3.12
```
