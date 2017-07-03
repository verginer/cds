#!/usr/bin/env bash
# run `chmod +x drop_jupyter_output.sh` to make it executable.

file=$(mktemp)
cat <&0 >$file
jupyter nbconvert --to notebook --ClearOutputPreprocessor.enabled=True \
    $file --stdout 2>/dev/null
