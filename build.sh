#!/bin/sh
# Builds build/create_nerfad-<version with dashes>.jar from create_nerfad/.
# The version comes from create_nerfad/fabric.mod.json.
set -e
cd "$(dirname "$0")"
VERSION=$(sed -n 's/.*"version": *"\([^"]*\)".*/\1/p' create_nerfad/fabric.mod.json)
rm -rf build
mkdir build
(cd create_nerfad && zip -q -r -X "../build/create_nerfad-$(echo "$VERSION" | tr . -).jar" . -x todo-after-fly-update.txt)
echo "built build/create_nerfad-$(echo "$VERSION" | tr . -).jar"
