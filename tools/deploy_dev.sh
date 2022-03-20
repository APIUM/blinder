#!/usr/bin/env bash
#
# Copy files in src/* to a target port
# Usage: tools/deploy_dev /dev/ttyUSB0

set -eo pipefail

[ "$#" -ge 1 ] || { echo "missing port"; exit 1; }

for f in src/*
do
    echo "Copying $f to $1"
	ampy -p "$1" -b 115200 put "$f"
done
