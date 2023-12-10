"""Day 7 module"""


class Day7:
    """Class for solving day 7 problem"""

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

        hand_types = {
            "high": [],
            "one": [],
            "two": [],
            "three": [],
            "full": [],
            "four": [],
            "five": [],
        }

        # Get the lines of input
        lines = self.file_reader.read_lines("day7/input.txt")
        # For each line start processing line
        for line in lines:
            data = line.split(" ")
            hand = data[0]
            bid = data[1]

            hand_data = {
                "hand": hand,
                "bid": bid,
            }

            hand_stats = {}
            for character in hand:
                if character not in hand_stats:
                    hand_stats[character] = 0

                hand_stats[character] += 1

            if len(hand_stats) == 1:
                # Five of a kind
                hand_types["five"].append(hand_data)
            elif len(hand_stats) == 5:
                # High card
                hand_types["high"].append(hand_data)
            else:
                counts = sorted(hand_stats.values(), reverse=True)

                if counts[0] == 4:
                    # Four of a kind
                    hand_types["four"].append(hand_data)
                elif counts[0] == 3:
                    if counts[1] == 2:
                        # Full house
                        hand_types["full"].append(hand_data)
                    else:
                        # 3 of a kind
                        hand_types["three"].append(hand_data)
                elif counts[0] == 2:
                    if counts[1] == 2:
                        # Two pair
                        hand_types["two"].append(hand_data)
                    else:
                        # One pair
                        hand_types["one"].append(hand_data)

        total = 0
        counter = 1
        for name, hand_info in hand_types.items():
            self.ui.print_warning(f"Working on {name} hand info")

            if len(hand_info) > 1:
                sorted_hand_info = self.sort_hands(hand_info)
            else:
                sorted_hand_info = hand_info

            self.ui.print_info(sorted_hand_info)

            for hand in sorted_hand_info:
                total += float(hand["bid"]) * counter
                counter += 1
                self.ui.print_info(f"New total is: {total}")

        self.ui.print_success(f"The total winnings are: {total}")

    def solve_problem_2(self):
        """Solve problem 2"""

    def sort_hands(self, hand_info):
        """Sort hands based on value"""

        conversion = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
        }

        def _custom_compare(hand1, hand2):
            for i in range(5):
                if conversion[hand1["hand"][i]] < conversion[hand2["hand"][i]]:
                    return -1
                elif conversion[hand1["hand"][i]] > conversion[hand2["hand"][i]]:
                    return 1
            return 0

        from functools import cmp_to_key

        sorted_hand_info = sorted(hand_info, key=cmp_to_key(_custom_compare))

        return sorted_hand_info
