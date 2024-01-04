#!/usr/bin/python3
import sys

argv = sys.argv

argc = len(argv)

print(f"Number of argument(s): {argc}")

if argc > 1:
    print(f"Argument(s):")
    for i in range(1, argc):
        print(f"{i}: {argv[i]}")
