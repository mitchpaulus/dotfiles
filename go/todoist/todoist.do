#!/bin/sh
redo-ifchange todoist.go
go build -o "$3" todoist.go
