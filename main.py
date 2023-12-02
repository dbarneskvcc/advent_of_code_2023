#!/usr/bin/env python
"""Main entry point definition"""
# System Imports
import re
import sys


def run(*args):
    """Main entry point for program"""
    print("Which input do you want to solve")
    print("1. input1")
    print("2. input2")
    choice = input()

    if choice == 1:
        with open("input.txt", "r") as file:
            lines = file.read().splitlines()

            total = 0
            for line in lines:
                numbers_only = re.sub("[^0-9]", "", line)
                # print(numbers_only)
                first_and_last = f"{numbers_only[0]}{numbers_only[-1]}"
                # print(first_and_last)
                total += int(first_and_last)

            print(f"The total is: {total}")

    else:
        number_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }
        with open("input.txt", "r") as file:
            lines = file.read().splitlines()

            total = 0
            for line in lines:
                # converted = line
                # for key, value in number_map.items():
                #     converted = converted.replace(key, value)
                # numbers_only = re.sub("[^0-9]", "", converted)
                # print(numbers_only)

                lowest_start_index = 200
                start = None
                highest_end_index = -1
                end = None
                for text in number_map.keys():
                    index = line.find(text)
                    if index == -1:
                        index = lowest_start_index
                    if index < lowest_start_index:
                        lowest_start_index = index
                        start = text
                for text in number_map.keys():
                    index = line.rfind(text)
                    if index == -1:
                        index = highest_end_index
                    if index > highest_end_index:
                        highest_end_index = index
                        end = text

                # print(line)
                start_int = number_map[start]
                end_int = number_map[end]
                full_number = f"{start_int}{end_int}"
                print(full_number)
                total += int(full_number)

                # first_and_last = f"{numbers_only[0]}{numbers_only[-1]}"
                # print(first_and_last)
                # total += int(first_and_last)

            print(f"The total is: {total}")

            # 55218


# Prevent running on import.
if __name__ == "__main__":
    run(*sys.argv[1:])
else:
    raise ImportError("Run this file directly, don't import it!")
