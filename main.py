#!/usr/bin/env python
"""Main entry point definition"""
# System Imports
import sys

from ui import UserInterface
from utils import FileReader
from day1 import Day1
from day2 import Day2
from day3 import Day3
from day4 import Day4
from day5 import Day5
from day6 import Day6
from day7 import Day7
from day8 import Day8
from day9 import Day9


def main():
    """Main entry point for program"""
    ui = UserInterface()
    file_reader = FileReader()
    ui.display_welcome_greeting()
    choice = ui.display_menu_and_get_response()

    while choice != UserInterface.MAX_MENU_CHOICES:
        if choice == 1:
            # Do Day 1
            day1 = Day1(ui, file_reader)
            day1.run()
        elif choice == 2:
            # Do Day 2
            day2 = Day2(ui, file_reader)
            day2.run()
        elif choice == 3:
            # Do Day 3
            day3 = Day3(ui, file_reader)
            day3.run()
        elif choice == 4:
            # Do Day 4
            day4 = Day4(ui, file_reader)
            day4.run()
        elif choice == 5:
            # Do Day 5
            day5 = Day5(ui, file_reader)
            day5.run()
        elif choice == 6:
            # Do Day 6
            day6 = Day6(ui, file_reader)
            day6.run()
        elif choice == 7:
            # Do Day 7
            day7 = Day7(ui, file_reader)
            day7.run()
        elif choice == 8:
            # Do Day 8
            day8 = Day8(ui, file_reader)
            day8.run()
        elif choice == 9:
            # Do Day 9
            day9 = Day9(ui, file_reader)
            day9.run()

        choice = ui.display_menu_and_get_response()


# Prevent running on import.
if __name__ == "__main__":
    main(*sys.argv[1:])
else:
    raise ImportError("Run this file directly, don't import it!")
