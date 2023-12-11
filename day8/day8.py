"""Day 8 module"""
from math import lcm


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
                print("Do you want to solve it fast or brute force?")
                print("1. Fast")
                print("2. Brute Force")
                sub_choice = self.ui.get_int("")
                if sub_choice == "2":
                    self.solve_problem_2_brute_force()
                else:
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

        self.ui.print_warning("Solving Problem 2 Fast Way")
        start_spots = []
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

                if key[-1] == "A":
                    start_spots.append(key)

        end_steps = []

        for start in start_spots:
            total_counter = 0
            counter = 0
            answer = start
            while answer[-1] != "Z":
                if counter == len(instructions):
                    counter = 0

                instruction = instructions[counter]
                answer = directions[answer][instruction]
                counter += 1
                total_counter += 1

            self.ui.print_info(
                f"The total number of steps for {start} was: {total_counter}"
            )
            end_steps.append(total_counter)

        final_total = lcm(*end_steps)

        self.ui.print_success(f"The total number of steps for all is: {final_total}")

    def solve_problem_2_brute_force(self):
        """Solve problem 2"""

        self.ui.print_warning("Solving Problem 2 Brute Force. It will never finish.")

        start_spots = []
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

                if key[-1] == "A":
                    start_spots.append(key)

        total_counter = 0
        counter = 0
        answers = [spot for spot in start_spots]
        self.ui.print_info("The start spots are:")
        self.ui.print_info(answers)

        while not self.check_for_end(answers):
            if counter == len(instructions):
                counter = 0

            instruction = instructions[counter]

            new_answers = []
            for answer in answers:
                new_answer = directions[answer][instruction]
                new_answers.append(new_answer)

            answers = new_answers

            counter += 1
            total_counter += 1

            print(f"iter: {total_counter} - {answers}", end="\r", flush=True)

        self.ui.print_success(f"The total number of steps was: {total_counter}")

    def check_for_end(self, answers):
        """Check to see if all answers are at the end"""
        result = True
        for answer in answers:
            if answer[-1] != "Z":
                result = False

        return result
