<https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.HTML>

user data files.          `$XDG_DATA_HOME`.   (`$HOME/.local/share`)
user configuration files. `$XDG_CONFIG_HOME`. (`$HOME/.config`)
user state data.          `$XDG_STATE_HOME`.  (`$HOME/.local/state)`
user executable files.                        (`$HOME/.local/bin`)

There is a set of preference ordered base directories relative to which data files should be searched. This set of directories is defined by the environment variable $XDG_DATA_DIRS.
There is a set of preference ordered base directories relative to which configuration files should be searched. This set of directories is defined by the environment variable $XDG_CONFIG_DIRS.
user-specific non-essential (cached) data. `$XDG_CACHE_HOME`. (`$HOME/.cache`)
user-specific runtime files and other file objects should be placed. `$XDG_RUNTIME_DIR`.
