#!/bin/bash

SOURCE=$1
DEST=$2

if [ -z "$SOURCE" ] || [ -z "$DEST" ]; then
    echo "Usage: $0 <source_directory> <destination_directory>"
    exit 1
fi

if [ ! -d "$SOURCE" ]; then
    echo "Error: Source directory '$SOURCE' does not exist."
    exit 1
fi

if [ ! -d "$DEST" ]; then
    echo "Destination '$DEST' not found. Creating it..."
    mkdir -p "$DEST"
fi

DATE=$(date +%F-%H-%M-%S)
BACKUP="$DEST/backup-$DATE.tar.gz"

tar -czf "$BACKUP" "$SOURCE"

echo "Backup completed: $BACKUP"
