#!/bin/sh

help() {
    cat <<EOF
foldersync_folder_creation.sh

Creates the following folders for a given BAS:
1. FailedToUpload
2. Logs
3. NeedToPreProcess
4. NeedToUpload
5. Uploaded
EOF
}

if test "$1" = "-h" || test "$1" = "--help"; then
    help
    exit 0
fi

mkdir -p FailedToUpload && mkdir -p Logs && mkdir -p NeedToPreProcess && mkdir -p NeedToUpload && mkdir -p Uploaded
