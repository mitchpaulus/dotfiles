# git

## File Permissions

In the past, I've had some issues with file permissions in the
interaction between WSL and git. The original WSL file system would make
all the files executable by default.

GIt files are either 644 (rw-r--r--) or 755 (rwxr-xr-x).

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


## Cleaning up a repository

From [https://www.git-scm.com/docs/gitattributes#_end_of_line_conversion](https://www.git-scm.com/docs/gitattributes#_end_of_line_conversion):

```sh
$ echo "* text=auto" >.gitattributes
$ git add --renormalize .
$ git status        # Show files that will be normalized
$ git commit -m "Introduce end-of-line normalization"
```

