"""Day 1 module"""

import re


class Day1:
    """Class for solving day 1 problem"""

    def __init__(self, ui):
        """Constructor"""
        self.ui = ui

    def run(self):
        """Run method"""
        choice = self.ui.display_problem_menu_and_get_response()
        while choice != self.ui.MAX_PROBLEM_MENU_CHOICES:
            if choice == 1:
                # Do Problem 1
                self.solve_problem_1()
            elif choice == 2:
                # Do Problem 2
                self.solve_problem_2()

            choice = self.ui.display_problem_menu_and_get_response()

    def solve_problem_1(self):
        """Solve problem 1"""
        with open("day1/input.txt", "r", encoding="utf8") as file:
            lines = file.read().splitlines()

            total = 0
            for line in lines:
                numbers_only = re.sub("[^0-9]", "", line)
                # print(numbers_only)
                first_and_last = f"{numbers_only[0]}{numbers_only[-1]}"
                # print(first_and_last)
                total += int(first_and_last)

            print(f"The total is: {total}")

            # 54951

    def solve_problem_2(self):
        """Solve problem 2"""
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
        with open("day1/input.txt", "r", encoding="utf8") as file:
            lines = file.read().splitlines()

            total = 0
            for line in lines:
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

                start_int = number_map[start]
                end_int = number_map[end]
                full_number = f"{start_int}{end_int}"
                total += int(full_number)

            print(f"The total is: {total}")

            # 55218
