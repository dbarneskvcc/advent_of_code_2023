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
        # Accumulator the total game numbers
        total = 0

        # Dict of the max quantity for each color in game
        max_colors = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }

        # Get the lines of input
        lines = self.file_reader.read_lines("day2/input.txt")
        # For each line start processing line
        for line in lines:
            # Split into parts
            game_parts = line.split(": ")
            # Get the game title from the left half
            game_title = game_parts[0]
            # Get game number from last part of game title
            game_number = int(game_title.split(" ")[-1])
            # Get the game string data from the right half of the line parts
            game_set_string = game_parts[1]
            # Split the game set string into game sets on semi-colon
            # Will produce a list of game sets.
            game_sets = game_set_string.split("; ")
            # Bool to know if all sets in game are okay and do not contain any
            # quantities over the max in the dict above.
            all_good = True
            # Loop over each game set. EX: 'red 2, green 4'
            for game_set in game_sets:
                # Get the color info for each set by splitting on the comma
                color_parts = game_set.split(", ")
                # Loop over each color part. EX: 'red 2'
                for color_part in color_parts:
                    # Split into color and quantity
                    game_set_parts = color_part.split(" ")
                    quantity = game_set_parts[0]
                    color = game_set_parts[1]
                    # If the quantity is greater than the max allowable value for that color.
                    if int(quantity) > max_colors[color]:
                        # Print error to screen
                        self.ui.print_error(
                            f"Game {game_number} is over with {color} = {quantity}"
                        )
                        # Flip all good flag to false
                        all_good = False
            # If after processing all sets for a game, the all_good is still True,
            # we have a valid game, otherwise, it is not valid.
            if all_good:
                # Print info message and add game number to total
                self.ui.print_info(f"Game {game_number} is good to go!")
                total += game_number

        # Print success and total
        self.ui.print_success(f"The total is: {total}")

    def solve_problem_2(self):
        """Solve problem 2"""
        # Accumulator the total power of each game
        total = 0

        # Get the lines of input
        lines = self.file_reader.read_lines("day2/input.txt")
        # For each line start processing line
        for line in lines:
            # Split into parts
            game_parts = line.split(": ")
            # Get the game title from the left half
            game_title = game_parts[0]
            # Get game number from last part of game title
            game_number = int(game_title.split(" ")[-1])
            # Get the game string data from the right half of the line parts
            game_set_string = game_parts[1]
            # Split the game set string into game sets on semi-colon
            # Will produce a list of game sets.
            game_sets = game_set_string.split("; ")

            # Define dict of max values for each color. Init to zero.
            max_for_game = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            # Loop over each game set. EX: 'red 2, green 4'
            for game_set in game_sets:
                # Get the color info for each set by splitting on the comma
                color_parts = game_set.split(", ")
                # Loop over each color part. EX: 'red 2'
                for color_part in color_parts:
                    # Split into color and quantity
                    game_set_parts = color_part.split(" ")
                    quantity = game_set_parts[0]
                    color = game_set_parts[1]

                    # If the current game set's color's quantity is more than
                    # the max we are keeping track of, update it to reflect the
                    # new larger number.
                    if max_for_game[color] < quantity:
                        max_for_game[color] = quantity

            # Print out info about each game's color max
            self.ui.print_info(f"Game {game_number} max red = {max_for_game['red']}")
            self.ui.print_info(
                f"Game {game_number} max green = {max_for_game['green']}"
            )
            self.ui.print_info(f"Game {game_number} max blue = {max_for_game['blue']}")

            # Calculate the power for the game
            power = max_for_game["red"] * max_for_game["green"] * max_for_game["blue"]
            # Print out info about the power for the game.
            self.ui.print_info(f"Game {game_number} power is: {power}")

            # Accumulate the power to the total var
            total += power

        # Print out success of answer.
        self.ui.print_success(f"The total is: {total}")
