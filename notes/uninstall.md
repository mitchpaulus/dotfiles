# Uninstall

## CMake trick

cmake leaves a `install_manifest.txt` file. Can use command

```
xargs rm < install_manifest.txt
```

to remove all files. See https://github.com/htacg/tidy-html5/issues/100#issuecomment-81063422
