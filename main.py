#!/usr/bin/env python
"""Main entry point definition"""
# System Imports
import re
import sys


def run(*args):
    """Main entry point for program"""
    # Call the main method for the program
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

        total = 0
        for line in lines:
            numbers_only = re.sub("[^0-9]", "", line)
            # print(numbers_only)
            first_and_last = f"{numbers_only[0]}{numbers_only[-1]}"
            # print(first_and_last)
            total += int(first_and_last)

        print(total)


# Prevent running on import.
if __name__ == "__main__":
    run(*sys.argv[1:])
else:
    raise ImportError("Run this file directly, don't import it!")
