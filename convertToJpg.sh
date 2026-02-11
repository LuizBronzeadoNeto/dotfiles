#!/bin/bash

# Input file
INPUT="$1"

# Check if provided
if [[ -z "$INPUT" ]]; then
    echo "Usage: tojpeg.sh <imagefile>"
    exit 1
fi

# Check file exists
if [[ ! -f "$INPUT" ]]; then
    echo "Error: File not found: $INPUT"
    exit 1
fi

# Get directory, basename, and output path
DIR="$(dirname "$INPUT")"
BASE="$(basename "$INPUT")"
NAME="${BASE%.*}"   # Remove extension

OUTPUT="${DIR}/${NAME}.jpg"

# Convert to JPEG
convert "$INPUT" "$OUTPUT"

echo "Output → $OUTPUT"

