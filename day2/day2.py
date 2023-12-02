"""Day 2 module"""


class Day2:
    """Class for solving day 2 problem"""

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
        total = 0
        max_colors = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        lines = self.file_reader.read_lines("day2/input.txt")
        for line in lines:
            # print(line)
            parts = line.split(": ")
            game_title = parts[0]
            game_number = int(game_title.split(" ")[-1])
            # print(game_number)
            games_string = parts[1]
            # print(games_string)

            game_sets = games_string.split("; ")
            # print(game_sets)

            all_good = True
            for color_info in game_sets:
                color_parts = color_info.split(", ")
                # game_set_stats = {}
                for color_part in color_parts:
                    game_set_parts = color_part.split(" ")
                    # game_set_stats[game_parts[1]] = game_parts[0]

                    # print(game_set_parts)
                    quantity = game_set_parts[0]
                    color = game_set_parts[1]
                    if int(quantity) > max_colors[color]:
                        self.ui.print_error(
                            f"Game {game_number} is over with {color} = {quantity}"
                        )
                        all_good = False

            if all_good:
                self.ui.print_info(f"Game {game_number} is good to go!")
                total += game_number

        self.ui.print_success(f"The total is: {total}")

    def solve_problem_2(self):
        """Solve problem 2"""
        total = 0

        lines = self.file_reader.read_lines("day2/input.txt")
        for line in lines:
            # print(line)
            parts = line.split(": ")
            game_title = parts[0]
            game_number = int(game_title.split(" ")[-1])
            # print(game_number)
            games_string = parts[1]
            # print(games_string)

            game_sets = games_string.split("; ")
            # print(game_sets)

            max_for_game = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            for color_info in game_sets:
                color_parts = color_info.split(", ")
                # game_set_stats = {}
                for color_part in color_parts:
                    game_set_parts = color_part.split(" ")
                    # game_set_stats[game_parts[1]] = game_parts[0]

                    # print(game_set_parts)
                    quantity = int(game_set_parts[0])
                    color = game_set_parts[1]

                    if max_for_game[color] < quantity:
                        max_for_game[color] = quantity

            self.ui.print_info(f"Game {game_number} max red = {max_for_game['red']}")
            self.ui.print_info(
                f"Game {game_number} max green = {max_for_game['green']}"
            )
            self.ui.print_info(f"Game {game_number} max blue = {max_for_game['blue']}")

            power = max_for_game["red"] * max_for_game["green"] * max_for_game["blue"]
            self.ui.print_info(f"Game {game_number} power is: {power}")

            total += power

        self.ui.print_success(f"The total is: {total}")
