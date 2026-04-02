#!/usr/bin/env python3

import sys

def search(pattern, filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if pattern in line:
                print(line.rstrip())

def main():
    if len(sys.argv) != 3:
        print("Usage: pygrep <pattern> <file>")
        sys.exit(1)

    pattern = sys.argv[1]
    filename = sys.argv[2]

    search(pattern, filename)

if __name__ == "__main__":
    main()
