"""User Interface module"""
# pylint: disable=pointless-statement
# System imports.


class UserInterface:
    """UserInterface class"""

    MAX_MENU_CHOICES = 26
    MAX_PROBLEM_MENU_CHOICES = 3

    # region public methods

    def display_welcome_greeting(self):
        """Display Welcome Greeting."""
        # change_color(Style.CYAN)
        Style.CYAN
        print("Welcome to Advent of Code")
        Style.RESET

    def display_menu_and_get_response(self):
        """Display Menu and get response."""

        # Display menu and prompt
        self._display_menu()

        # Get the selection they enter
        selection = int(self.get_int(""))

        # While the response is not valid.
        while not (selection > 0 and selection <= self.MAX_MENU_CHOICES):
            # Display error message.
            self.print_error("Not a valid choice.")
            # Get selection again.
            selection = int(self.get_int(""))

        # Return the selection casted to an int
        return int(selection)

    def display_problem_menu_and_get_response(self):
        """Display Problem menu and get response"""

        # Display menu and prompt
        self._display_problem_menu()

        # Get the selection they enter
        selection = int(self.get_int(""))

        # While the response is not valid.
        while not (selection > 0 and selection <= self.MAX_PROBLEM_MENU_CHOICES):
            # Display error message.
            self.print_error("Not a valid choice.")
            # Get selection again.
            selection = int(self.get_int(""))

        # Return the selection casted to an int
        return int(selection)

    def print(self, message):
        """Display message"""
        print(message)

    def print_info(self, message):
        """Display info message."""
        Style.CYAN
        print(message)
        Style.RESET

    def print_success(self, message):
        """Display success message."""
        Style.GREEN
        print(message)
        Style.RESET

    def print_warning(self, message):
        """Display warning message."""
        Style.YELLOW
        print(message)
        Style.RESET

    def print_error(self, message):
        """Display error message."""
        Style.RED
        print(message)
        Style.RESET

    def get_str(self, message):
        """Get a valid string field from the console."""
        print(message)
        self._display_prompt()
        valid = False
        while not valid:
            value = input()
            if value:
                valid = True
            else:
                Style.RED
                print("You must provide a value.")
                Style.RESET
                print()
                print(message)
                self._display_prompt()
        return str(value)

    def get_int(self, message):
        """Get a valid Int field from the console."""
        print(message)
        self._display_prompt()
        valid = False
        while not valid:
            try:
                value = int(input())
                valid = True
            except ValueError:
                Style.RED
                print("That is not a valid Integer. Please enter a valid Integer.")
                Style.RESET
                print()
                print(message)
                self._display_prompt()
        return str(value)

    def get_decimal(self, message):
        """Get a valid Decimal field from the console."""
        print(message)
        self._display_prompt()
        valid = False
        while not valid:
            try:
                value = float(input())
                valid = True
            except ValueError:
                Style.RED
                print("That is not a valid Decimal. Please enter a valid Decimal.")
                Style.RESET
                print()
                print(message)
                self._display_prompt()
        return str(value)

    def get_bool(self, message):
        """Get a valid Bool field from the console."""
        print(message)
        self._display_prompt()
        valid = False
        while not valid:
            user_input = input()
            if user_input.lower() == "y" or user_input.lower() == "n":
                valid = True
                value = user_input.lower() == "y"
            else:
                Style.RED
                print("That is not a valid Entry.")
                Style.RESET
                print()
                print(message)
                self._display_prompt()

        return str(value)

    # endregion

    # region private methods

    def _display_prompt(self):
        """Display the prompt"""
        print("> ", end="")

    def _display_menu(self):
        """Display the Menu"""
        print()
        print("Which day would you like to run?")
        print()
        print("1. Day One")
        print("2. Day Two")
        print("3. Day Three")
        print("4. Day Four")
        print("5. Day Five")
        # print("6. Day Six")
        # print("7. Day Seven")
        # print("8. Day Eight")
        # print("9. Day Nine")
        # print("10. Day Ten")
        # print("11. Day Eleven")
        # print("12. Day Twelve")
        # print("13. Day Thirteen")
        # print("14. Day Fourteen")
        # print("15. Day Fifteen")
        # print("16. Day Sixteen")
        # print("17. Day Seventeen")
        # print("18. Day Eighteen")
        # print("19. Day Nineteen")
        # print("20. Day Twenty")
        # print("21. Day Twenty One")
        # print("22. Day Twenty Two")
        # print("23. Day Twenty Three")
        # print("24. Day Twenty Four")
        # print("25. Day Twenty Five")
        print("26. Exit Program")

    def _display_problem_menu(self):
        """Display the problem menu"""
        print()
        print("Which problem would you like to run?")
        print()
        print("1. Problem One")
        print("2. Problem Two")
        print("3. Return to previous menu")

    def _display_main_prompt(self):
        """Display the Prompt"""
        print()
        print("Enter Your Choice:")
        self._display_prompt()

    def _get_selection(self):
        """Get the selection from the user."""
        return input()

    def _verify_selection_valid(self, selection):
        """Verify that a selection from the main menu is valid."""
        return_value = False
        # If the choice is between 0 and the MAX_MENU_CHOICES
        if selection > 0 and selection <= self.MAX_MENU_CHOICES:
            # Set the return value to True
            return_value = True

        # Return the return_value
        return return_value

    # endregion


# Decorator to convert Style class to a Singleton
def singleton(cls):
    return cls()


# Class of different Styles
@singleton
class Style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

    def __getattribute__(self, name):
        """Override default dunder method"""
        value = super().__getattribute__(name)
        print(value, end="")
        return value
