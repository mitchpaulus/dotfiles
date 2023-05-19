# git

## File Permissions

In the past, I've had some issues with file permissions in the interaction between WSL and git.
The original WSL file system would make all the files executable by default.

Git files are either 644 (rw-r--r--) or 755 (rwxr-xr-x).

## Line Endings

My gosh, why does this have to be so complicated.

Definition of "normalization", from the git documentation:

> When a text file is normalized, its line endings are converted to LF in the repository.

## `.gitattributes` file

`text` attribute:
- Set: Force the file to be normalized

- Unset: Does not normalize upon check-in or checkout

- text=auto: When text is set to "auto", the path is marked for
             automatic end-of-line conversion. If Git decides that the content is
             text, its line endings are converted to LF on checkin. When the file
             has been committed with CRLF, no conversion is done.
- Unspecified: Git uses the `core.autocrlf` configuration variable to determine if the file should be converted.

`eol` attribute:

- Set to "crlf" - Windows line endings in the working files
- Set to "lf" - Unix line endings in the working files

Fixing after setting up .gitattributes (from <https://git-scm.com/docs/gitattributes#_end_of_line_conversion>)

```
$ echo "* text=auto" >.gitattributes
$ git add --renormalize .
$ git status        # Show files that will be normalized
$ git commit -m "Introduce end-of-line normalization"
```

## Cleaning up a repository

From <https://www.git-scm.com/docs/gitattributes#_end_of_line_conversion>:

```sh
$ echo "* text=auto" >.gitattributes
$ git add --renormalize .
$ git status        # Show files that will be normalized
$ git commit -m "Introduce end-of-line normalization"
```

## Extracting a folder to own repository

TLDR: `git filter-repo --path 'path/to/folder' --path-rename '/path/to/folder/:'`

Uses [git-filter-repo](https://github.com/newren/git-filter-repo).
Figured out the right path rename from [here](https://making.close.com/posts/splitting-sub-folders-out-into-new-git-repository).
Also see: <https://docs.github.com/en/get-started/using-git/splitting-a-subfolder-out-into-a-new-repository>


## Remove Untracked files

`git clean -d -n` to dry run. `git clean -d -i` for interactive delete,
`-f` option to force the deletion.

## Move Remote

`git remote set-url <remote> <URL>`

## Show configuration options

```sh
git config --list --show-origin
```


```
/etc/gitconfig or C:\ProgramData\Git\etc\config # System

$XDG_CONFIG_HOME/git/config  or %USERPROFILE%/.gitconfig # Global (also called user)
~/.gitconfig # Global (also called user)
~/.config/git/config

${GIT_DIR:.git}/config # Local

$GIT_DIR/config.worktree # Worktree
```


## Recovering lost files

This one really saved my behind (<https://stackoverflow.com/a/1109433/5932184>):

```console
$ git fsck --cache --no-reflogs --lost-found --dangling HEAD
```

This prints out a whole bunch of hashes for blob (and commits and other stuff).

I then looped over the blobs and got the contents using `git show <sha>`, redirecting to a backup file.

## Pushing a tag

```
git push origin v0.1.0
```

## Remove Tag

```
git tag -d tagname # local
git push origin --delete tagname # remote
removetag tagname # myscript
```

## Mode Changes

```
git update-index --chmod=+x files..
```

Dealing with file permissions with GitHub desktop: <https://stackoverflow.com/a/41368342/5932184>

- delete the line setting core.filemode in $projdir/.git/config
- in Windows git, run "git config --global core.filemode false"
