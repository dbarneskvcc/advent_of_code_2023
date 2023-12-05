"""Day 4 module"""
import re


class Day4:
    """Class for solving day 3 problem"""

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

        # Total accumulator
        total = 0
        # Get the lines of input
        lines = self.file_reader.read_lines("day4/input.txt")
        # For each line start processing line
        for line in lines:
            # Strip out all extra whitespace so it is just a single between things.
            line = re.sub(" +", " ", line)
            # Split by the pipe to segregate the winning numbers from the Elf's numbers
            parts = line.split(" | ")
            # Get the winning numbers by splitting on the colon and taking the right side.
            winning_numbers = parts[0].split(": ")[1]
            # Convert to a list by splitting on the space between numbers
            winning_numbers = winning_numbers.split(" ")
            # Take the right half of the first split as the Elf's numbers
            elfs_numbers = parts[1]
            # Convert to a list by splitting on the space between numbers
            elfs_numbers = elfs_numbers.split(" ")

            # Get the intersection between the winning and the Elfs
            intersection = self.intersection(winning_numbers, elfs_numbers)
            self.ui.print_info(f"The matches are: {intersection}")
            # Get the number of matches as the length of the intersection
            number_of_matches = len(intersection)
            self.ui.print_info(f"Number of matches: {number_of_matches}")
            # Init points to 0
            points = 0
            # If matches are greater than 0, we can calculate them, otherwise skip.
            # NOTE: Not doing it this way would make 0 matches have 1 point.
            if number_of_matches > 0:
                # Calc points by taking 2 and raising it to the length - 1.
                # 1 match = 2^0 = 1
                # 2 matches = 2^1 = 2
                # 3 matches = 2^3 = 4
                # Etc.
                points = 2 ** (number_of_matches - 1)
            self.ui.print_info(f"Number of points: {points}")

            # Accumulate the points
            total += points

        # Print the result
        self.ui.print_success(f"The total is: {total}")

    def solve_problem_2(self):
        """Solve problem 2"""

        raise Exception()

    def intersection(self, list1, list2):
        return [value for value in list2 if value in list1]
