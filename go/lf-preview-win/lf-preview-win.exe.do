#!/usr/bin/env mshell
[redo-ifchange lf-preview-win.go];
'windows' $GOOS!
'amd64' $GOARCH!
['go' 'build' '-o' $3 lf-preview-win.go];
