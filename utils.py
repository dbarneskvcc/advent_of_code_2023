"""Utils module"""


class FileReader:
    """File reader"""

    def read_lines(self, path):
        """Read the lines of the file and return list of them"""
        lines = []
        with open(path, "r", encoding="utf8") as file:
            lines = file.read().splitlines()
        return lines
