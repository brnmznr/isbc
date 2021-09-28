#!/bin/bash

_autolaunch_dir="${HOME}/Library/Application Support/iTerm2/Scripts/AutoLaunch"
mkdir -p "${_autolaunch_dir}"

echo "AutoLaunch folder: '${_autolaunch_dir}'"

echo "Cleanup AutoLaunch folder"
find "${_autolaunch_dir}" -type l -name '*.py' -delete

echo "Linking scripts to AutoLaunch folder"
for item in $(ls *.py); do
  echo " Linking ${item}..."
  ln -s $(pwd)/$item "${_autolaunch_dir}/${item}"
done
