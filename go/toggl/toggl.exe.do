#!/usr/bin/env mshell
[redo-ifchange toggl.go];
'windows' $GOOS!
'amd64' $GOARCH!
['go' 'build' '-o' $3 toggl.go];
