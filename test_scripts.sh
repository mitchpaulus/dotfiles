#!/bin/sh
for file in scripts/*; do
    if has_sh_shebang "$file"; then
        shellcheck "$file"
    fi
done
