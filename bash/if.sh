#!/bin/bash

# Check if a directory does exist
if [ -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY exists.
fi

# Check if directory does not exist
if [ ! -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
fi

# To check for symbolic links
if [ -d "$LINK_OR_DIR" ]; then 
  if [ -L "$LINK_OR_DIR" ]; then
    # It is a symlink!
    # Symbolic link specific commands go here.
    rm "$LINK_OR_DIR"
  else
    # It's a directory!
    # Directory command goes here.
    rmdir "$LINK_OR_DIR"
  fi
fi

# Simple if ifel else example
function serviceCheck () {
  # Checks to see if a service is running.
  service="${1}"
  status="$(systemctl is-active ${service})"
  #echo "${service} is: ${status}"
  if [ $status == "active" ]; then
    echo "service is active"
  elif [ $status == "inactive" ]; then
    echo "service is not active"
  else 
    echo "There was an error"
  fi
}
serviceCheck "networking"

# Checks if root
if ! [ $(id -u) = 0 ]; then
   echo "I am not root!"
   exit 1
fi