"""Day 4 module"""
import re


class Day4:
    """Class for solving day 4 problem"""

    def __init__(self, ui, file_reader):
        """Constructor"""
        self.ui = ui
        self.file_reader = file_reader

        self.original_cards = {}

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

        # Total accumulator
        total_card_count = 0
        # Get the lines of input
        lines = self.file_reader.read_lines("day4/input.txt")
        # Create a card counter
        counter = 1
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

            # Put number of matches into a dict keyed by the counter.
            # In the end of looping we will have a dict of:
            # Card #: Number of matches
            self.original_cards[counter] = number_of_matches
            # Increment card counter
            counter += 1

        # Now that we have the dict created, we can loop over the dict and
        # for each card number in it, work on figuring out what other cards
        # it will win for us.
        for card_number in self.original_cards:
            self.ui.print_info("--------------------------------")
            # Calculate the additional cards using recursion.
            additional_cards = self.calculate_cards_won(card_number)
            self.ui.print_info(f"{additional_cards} Additional Cards")
            self.ui.print_info("--------------------------------")

            # Accumulate the additional cards, plus 1 for the card we are
            # currently processing from the original list.
            total_card_count += additional_cards + 1

        # Print the result
        self.ui.print_success(f"The total is: {total_card_count}")

    def intersection(self, list1, list2):
        """Calculate the intersection between the two lists"""
        return [value for value in list2 if value in list1]

    def calculate_cards_won(self, card_number):
        """Recursive method to calculate the number of cards a card will win"""
        # Get the number of cards from the original cards dict
        number_of_won_cards = self.original_cards[card_number]
        # Init a loop counter based on the number of cards won
        loop_counter = number_of_won_cards
        # Set the card number counter to the current card number plus 1
        card_number_counter = card_number + 1
        # Init additional cards to zero
        additional_cards = 0
        # While we have not processed each of the cards that we won
        # EX: Card 1 has 4 matches, so it must process card 2, 3, 4, and 5. Loop 4 times.
        while loop_counter > 0:
            # Get the additional cards using recursion.
            # EX: First time through the loop it will have card number 2
            # This is based on card 1 entering method first time and then
            # being incremented above.
            additional_cards += self.calculate_cards_won(card_number_counter)
            # Decrement the loop counter as we only want to recursively call for
            # the number of cards we won.
            # NOTE: This also serves as our base case control for recursion.
            loop_counter -= 1
            # Increment the card number counter so that on the next time through
            # the loop we consider the next card.
            # EX: card was 2 above, we now need to make it card 3.
            card_number_counter += 1
        # Return the number of won cards plus any additional ones.
        return number_of_won_cards + additional_cards
