"""Day 8 module"""


class Day8:
    """Class for solving day 8 problem"""

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

        start = "AAA"
        end = "ZZZ"
        instructions = []
        directions = {}

        # Get the lines of input
        lines = self.file_reader.read_lines("day8/input.txt")
        # For each line start processing line
        for i, line in enumerate(lines):
            if i == 0:
                # Process steps
                line = line.replace("L", "0").replace("R", "1")
                for character in line:
                    if character == "0":
                        instructions.append(0)
                    else:
                        instructions.append(1)
            elif i == 1:
                continue
            else:
                parts = line.split(" = ")
                key = parts[0]
                values = parts[1].replace("(", "").replace(")", "").split(", ")
                value = tuple(val for val in values)

                directions[key] = value

        total_counter = 0
        counter = 0
        answer = start
        while answer != end:
            if counter == len(instructions):
                counter = 0

            instruction = instructions[counter]
            answer = directions[answer][instruction]
            counter += 1
            total_counter += 1

        self.ui.print_success(f"The total number of steps was: {total_counter}")

    def solve_problem_2(self):
        """Solve problem 2"""
