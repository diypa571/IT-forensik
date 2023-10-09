#!/bin/bash
# Diyar Parwana
# It is a very powerful script with a single command line to get file signature
# Get file signature, deleted, removed files...
# 
# Check if the user provided a directory path as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 /path/to/directory"
    exit 1
fi

directory="$1"

# Check if the specified directory exists
if [ ! -d "$directory" ]; then
    echo "Directory not found: $directory"
    exit 1
fi

# Use find to generate SHA-256 hashes for all files in the directory
find "$directory" -type f -exec sha256sum {} \;
