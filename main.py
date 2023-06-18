#!/usr/bin/env python3

from utils.tostring import ToString
from utils.maze import Maze

def main() -> None:
    """
    The main function for testing the maze generator.
    """

    rows = 10
    cols = 10

    maze = Maze(rows, cols)

    maze.generate()

    maze.to_string(delay=False)

if __name__ == "__main__":
    main()