"""Day 1 module"""

import re


class Day1:
    """Class for solving day 1 problem"""

    def __init__(self, ui, file_reader):
        """Constructor"""
        self.ui = ui
        self.file_reader = file_reader

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

        # Accumulator the total of concatenated numbers.
        total = 0
        # Get the lines of input
        lines = self.file_reader.read_lines("day1/input.txt")
        # For each line start processing line
        for line in lines:
            # Strip out all non-number characters
            numbers_only = re.sub("[^0-9]", "", line)
            # Get the first and last concatenated together.
            first_and_last = f"{numbers_only[0]}{numbers_only[-1]}"
            # Accumulate the total
            total += int(first_and_last)
        # Print success message of total
        self.ui.print_success(f"The total is: {total}")

    def solve_problem_2(self):
        """Solve problem 2"""

        # Make map of text numbers and digit numbers to digit numbers
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
        # Accumulator the total of concatenated numbers.
        total = 0
        # Get the lines of input
        lines = self.file_reader.read_lines("day1/input.txt")
        # For each line start processing line
        for line in lines:
            # Init lowest_start_index to something really high like 200
            lowest_start_index = 200
            # Init start value to None
            start = None
            # Init highest_end_index to something really low like -1
            # NOTE: Needs to be below zero as zero could be valid.
            highest_end_index = -1
            # Init end value to None
            end = None
            # Loop through all the key values in the number map.
            for text in number_map.keys():
                # Get the index of the key (text number or digit)
                index = line.find(text)
                # If the index is -1, the number was not found
                if index == -1:
                    # Set index to the current lowest_start as that will
                    # prevent anything from happening below.
                    index = lowest_start_index

                # If the index is less than the lowest start index
                # set the lowest start index to this index.
                if index < lowest_start_index:
                    lowest_start_index = index
                    # Also retrieve the number in that spot.
                    # NOTE: Will still be either a number string or a digit.
                    start = text

            # Loop through all the key values in the number map.
            for text in number_map.keys():
                # Get the index of the key (text number or digit)
                index = line.rfind(text)
                # If the index is -1, the number was not found
                if index == -1:
                    # Set index to the current highest_end as that will
                    # prevent anything from happening below.
                    index = highest_end_index
                # Do the same for the end value.
                # If the index is greater than the highest end index
                # set the highest end index to this index.
                if index > highest_end_index:
                    highest_end_index = index
                    # Also retrieve the number in that spot.
                    # NOTE: Will still be either a number string or a digit.
                    end = text

            # Use the start and end text in the number map to get the correct
            # corresponding digit to be used in the final concatenated number.
            start_int = number_map[start]
            end_int = number_map[end]
            # Create concatenated number
            full_number = f"{start_int}{end_int}"
            # Convert to int and add to the total
            total += int(full_number)

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")
