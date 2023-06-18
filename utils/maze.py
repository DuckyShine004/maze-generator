from collections import defaultdict
from collections import deque

from random import randint

from typing import List, Set, Tuple

from utils.tostring import ToString

class Maze:
    """
    The Maze class is an object created to call useful functions which
    are important for generating a maze. The randomized depth first
    search algorithm is used to generate the maze.

    Keywords:
    rows - the height of the maze.
    cols - the width of the maze.

    Attributes:
    __rows - a private field copy of rows.
    __cols - a private field copy of cols.
    __path - a private field list which stores the path of the generated maze.
    """

    def __init__(self, rows: int, cols: int) -> None:
        self.__rows = rows
        self.__cols = cols

        self.__path = []

    def dfs(self, u: int, v: int, visited: Set[Tuple[int, int]]) -> None:
        """
        Create a path using the randomized depth first search algorithm.
        Although unintuitive, we will use a y-x coordinate system.

        Keyword:
        u - the starting y coordinate.
        v - the strating x coordinate.
        visited - a set of visited nodes.
        """

        stack = deque()

        node = (u, v)

        stack.append(node)
        visited.add(node)

        while stack:
            node = stack[-1]
            self.add_to_path(node)

            neighbors = self.get_neighbors(node, visited)

            if neighbors:
                neighbor = neighbors[randint(0, len(neighbors) - 1)]

                stack.append(neighbor)
                visited.add(neighbor)
            else:
                stack.pop()

    def add_to_path(self, node: Tuple[int, int]) -> None:
        """
        Adds the passed node to the path.
        """

        self.__path.append(node)

    def clear_path(self) -> None:
        """
        Clear the path to create a new path; we want to create a new maze.
        """

        self.__path.clear()

    def get_path(self) -> List[Tuple[int, int]]:
        """
        Return the path, that is, the list of traversed nodes.
        """

        return self.__path

    def get_neighbors(
        self, node: Tuple[int, int], visited: Set[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        """
        Get all available adjacent neighbor nodes given the current node.

        Return the list of all available adjacent neighbor nodes.

        Keywords:
        node - a tuple of y-x coordinate.
        visited- the set of visited nodes.
        """

        neighbors = []

        u, v = node

        node_s = (u + 1, v)
        node_n = (u - 1, v)
        node_e = (u, v + 1)
        node_w = (u, v - 1)

        if self.check_neighbor(node_s, visited):
            neighbors.append(node_s)

        if self.check_neighbor(node_n, visited):
            neighbors.append(node_n)

        if self.check_neighbor(node_e, visited):
            neighbors.append(node_e)

        if self.check_neighbor(node_w, visited):
            neighbors.append(node_w)

        return neighbors

    def check_neighbor(
        self, node: Tuple[int, int], visited: Set[Tuple[int, int]]
    ) -> bool:
        """
        Check if the queried neighbor node is available. It is available if
        it has not been visited yet or it is within the width and height limit.

        Return a Boolean value, based on if the queried neighbor node is available.

        Keywords:
        node - a tuple of y-x coordinate.
        visited - the set of visited nodes.
        """

        y, x = node

        if node not in visited:
            if self.check_horizontal(x) and self.check_vertical(y):
                return True

        return False

    def check_horizontal(self, x: int) -> bool:
        """
        Check if the x coordinate is within the width of the maze.

        Return a Boolean value based on the consequent condition.

        Keywords:
        x - the passed x coordinate value.
        """

        return True if x >= 0 and x < self.__cols else False

    def check_vertical(self, y: int) -> bool:
        """
        Check if the y coordinate is within the width of the maze.

        Return a Boolean value based on the consequent condition.

        Keywords:
        y - the passed y coordinate value.
        """

        return True if y >= 0 and y < self.__rows else False

    def generate(self) -> None:
        """
        Upon function call; generates a maze.
        """

        self.clear_path()

        y = 0
        x = 0

        visited = set()

        self.dfs(y, x, visited)

    def to_string(self, delay: bool = False) -> None:
        """
        Displays the current generated maze in the form of concatenated strings.

        WARNING:
        the generate() function must be called first.

        Keywords:
        delay - a Boolean value that decides whether the user wants to see the
        maze creation at each iteration. The default value is False.
        """

        ToString(self.__rows, self.__cols).create_string(self.get_path(), delay)
