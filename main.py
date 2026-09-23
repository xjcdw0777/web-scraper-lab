#!/usr/bin/env python3
"""Entry point for the project."""

import sys
from utils import timer, file_size


@timer
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file>")
        sys.exit(1)
    
    path = sys.argv[1]
    try:
        size = file_size(path)
        print(f"File size: {size}")
    except FileNotFoundError:
        print(f"Error: {path} not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
