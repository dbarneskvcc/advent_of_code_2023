"""Day 5 module"""


class Day5:
    """Class for solving day 5 problem"""

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

        maps = {}
        seeds = []
        # Get the lines of input
        lines = self.file_reader.read_lines("day5/input.txt")
        dict_name = "START"
        # For each line start processing line
        for line in lines:
            if line == "":
                continue
            elif "seeds:" in line:
                seed_data = line.split("seeds: ")[1]
                seeds = seed_data.split(" ")
                seeds = [int(seed) for seed in seeds]
                self.ui.print_warning("Seeds:")
                self.ui.print_info(seeds)
            elif " map:" in line:
                dict_name = line.split(" map:")[0]
                self.ui.print_warning(dict_name)
                maps[dict_name] = []
            else:
                data_parts = line.split(" ")
                self.ui.print_info(data_parts)
                destination_range_start = int(data_parts[0])
                source_range_start = int(data_parts[1])
                range_length = int(data_parts[2])

                maps[dict_name].append(
                    {
                        "source_start": source_range_start,
                        "dest_start": destination_range_start,
                        "length": range_length,
                    }
                )

        all_valid_location_numbers = []

        for seed in seeds:
            self.ui.print_error(f"Working on seed {seed}")
            start_value = seed
            next_value = None
            for name, mapping in maps.items():
                self.ui.print_warning(f"Working on {name} conversion.")
                next_value = None
                for entry in mapping:
                    answer = self._get_next_value(
                        start_value,
                        entry["source_start"],
                        entry["dest_start"],
                        entry["length"],
                    )
                    print(answer)
                    if answer is not None:
                        next_value = answer
                        break

                if next_value is None:
                    next_value = start_value

                self.ui.print_info(f"Found conversion: {start_value} => {next_value}")

                start_value = next_value

            end_value = next_value

            all_valid_location_numbers.append(end_value)
            self.ui.print_success(f"The location number is: {end_value}")

        all_valid_location_numbers.sort()
        smallest = all_valid_location_numbers[0]

        self.ui.print_success(f"The lowest location number is: {smallest}")

    def solve_problem_2(self):
        """Solve problem 2"""

    def _get_next_value(self, source_val, source_start, dest_start, length):
        """Get the next value based on the dict info"""
        source_end = source_start + length
        if source_start <= source_val < source_end:
            diff = source_val - source_start
            result = dest_start + diff
            return result
        return None
