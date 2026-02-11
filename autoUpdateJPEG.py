#!/usr/bin/env python3
import os
import subprocess

WALL_DIR = os.path.expanduser("~/Wallpapers/walls")
CONVERTER = os.path.expanduser("~/Wallpapers/convertToJpg.sh")

def is_jpg(filename):
    return filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg")

def main():
    for filename in os.listdir(WALL_DIR):
        filepath = os.path.join(WALL_DIR, filename)

        # Skip directories
        if not os.path.isfile(filepath):
            continue

        # Skip already JPG/JPEG files
        if is_jpg(filename):
            continue

        print(f"Converting: {filename}")

        # Call your converter script
        subprocess.run([CONVERTER, filepath])

if __name__ == "__main__":
    main()
