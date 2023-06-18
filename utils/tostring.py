from collections import defaultdict

from typing import List, Tuple

from time import sleep

class ToString:
    """
    The ToString class is an object that is useful for calling string related
    functions.

    Keywords:
    rows - the height of the maze.
    cols - the width of the maze.

    Attributes:
    __to_string_maze - a private field dictionary that stores the maze in string form. 
    __rows - a private field copy of rows.
    __cols - a private field copy of cols.

    Function calls:
    initialize() - store the maze in string form.
    """

    def __init__(self, rows: int, cols: int):
        self.__to_string_maze = defaultdict(list)

        self.__rows = rows
        self.__cols = cols

        self.initialize()

    def to_string(self) -> None:
        """
        Displays the current generated maze in the form of concatenated strings.
        """

        print(" _" * self.__cols)

        for row in range(self.__rows):
            print("|", end="")
            print("".join(self.__to_string_maze[row]))

        print()

    def create_string(self, path: List[Tuple[int, int]], delay: bool = False) -> None:
        """
        Create the maze in the form of a string. 
        """

        for i in range(len(path) - 1):
            if delay:
                self.to_string()
                sleep(0.05)

            u = path[i]
            v = path[i + 1]

            r = v[0] - u[0]
            c = v[1] - u[1]

            if r != 0:
                if r > 0:
                    self.set_string(u[0], u[1], "_")
                else:
                    self.set_string(v[0], v[1], "_")

            if c != 0:
                if c > 0:
                    self.set_string(u[0], u[1], "|")
                else:
                    self.set_string(v[0], v[1], "|")

        if not (delay):
            self.to_string()

        print("Maze generated")

    def initialize(self) -> None:
        """
        Setup a hashmap to store the maze in the form of a string.
        """

        for row in range(self.__rows):
            for col in range(self.__cols):
                self.__to_string_maze[row].append("_|")

    def set_string(self, row: int, col: int, string: str) -> None:
        """
        Removes a wall based on the given the passed row, column, string values.

        Keywords:
        row - the passed row value.
        col - the passed column value.
        string - the wall (in the form of a string) to be removed.
        """

        self.__to_string_maze[row][col] = self.__to_string_maze[row][col].replace(string, " ")