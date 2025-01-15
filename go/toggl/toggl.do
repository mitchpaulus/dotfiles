#!/bin/sh
redo-ifchange toggl.go
go build -o "$3" toggl.go
