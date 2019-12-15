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
