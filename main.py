#!/usr/bin/env python
"""Main entry point definition"""
# System Imports
import sys

from ui import UserInterface
from utils import FileReader
from day1 import Day1
from day2 import Day2
from day3 import Day3


def main():
    """Main entry point for program"""
    ui = UserInterface()
    file_reader = FileReader()
    ui.display_welcome_greeting()
    choice = ui.display_menu_and_get_response()

    while choice != UserInterface.MAX_MENU_CHOICES:
        if choice == 1:
            # Do Day 1
            day1 = Day1(ui)
            day1.run()
        elif choice == 2:
            # Do Day 2
            day2 = Day2(ui, file_reader)
            day2.run()
        elif choice == 3:
            # Do Day 3
            day3 = Day3(ui)
            day3.run()

        choice = ui.display_menu_and_get_response()


# Prevent running on import.
if __name__ == "__main__":
    main(*sys.argv[1:])
else:
    raise ImportError("Run this file directly, don't import it!")
