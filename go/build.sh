#!/bin/sh

go build toggl.go
go build todoist.go

binlink toggl/toggl
binlink todoist/todoist
