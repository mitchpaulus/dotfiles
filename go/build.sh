#!/bin/bash
set -e

redo toggl/toggl todoist/todoist

pushd toggl
binlink toggl
popd

pushd todoist
binlink todoist
popd
