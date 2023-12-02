"""Day 5 module"""


class Day5:
    """Class for solving day 3 problem"""

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

    def solve_problem_2(self):
        """Solve problem 2"""