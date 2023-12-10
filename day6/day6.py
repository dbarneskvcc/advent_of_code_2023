"""Day 6 module"""
import re


class Day6:
    """Class for solving day 6 problem"""

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

        # Race list
        races = []
        # Get the lines of input
        lines = self.file_reader.read_lines("day6/input.txt")
        # For each line start processing line
        race_time_line = lines[0]
        race_distance_line = lines[1]

        time_data = race_time_line.split(":")[1]
        time_data = re.sub(" +", " ", time_data)[1:]
        time_data = time_data.split(" ")

        distance_data = race_distance_line.split(":")[1]
        distance_data = re.sub(" +", " ", distance_data)[1:]
        distance_data = distance_data.split(" ")

        for i, time in enumerate(time_data):
            races.append(
                {
                    "time": int(time),
                    "distance": int(distance_data[i]),
                    "ways_to_win": 0,
                }
            )

        for entry in races:
            time = entry["time"]
            distance = entry["distance"]
            for i in range(entry["time"]):
                answer = i * (time - i)
                if answer > distance:
                    entry["ways_to_win"] += 1

        total = 1
        for entry in races:
            total = total * entry["ways_to_win"]

        self.ui.print_success(f"The total is: {total}")

    def solve_problem_2(self):
        """Solve problem 2"""
