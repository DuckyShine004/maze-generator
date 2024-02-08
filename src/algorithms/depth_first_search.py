"""This module allows for maze generation with the randomized depth first 
search algorithm.
"""

from typing import TYPE_CHECKING, List, Tuple

import random

from collections import deque

from src.algorithms.algorithm import Algorithm

from src.utilities.utility import Utility

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT

if TYPE_CHECKING:
    from src.models.graph.graph import Graph


class DepthFirstSearch(Algorithm):
    """This class initializes the DepthFirstSearch object. A maze, believe it
    or not, can be generated with the randomized randomized depth first search
    algorithm."""

    def __init__(self, graph: "Graph"):
        """the Depth First Search algorithm object.

        Args:
            graph (Graph): The singleton graph object.
        """

        super().__init__(graph)

    def get_path(self) -> List[Tuple[int, int]]:
        """Returns a list of nodes (the path).

        Returns:
            List[Tuple[int, int]]: A list of nodes (path).
        """

        visited = [[False] * MAZE_HEIGHT for _ in range(MAZE_WIDTH)]

        start = Utility.get_random_position()
        stack = deque([start])
        path = deque()

        while stack:
            node = stack[-1]
            neighbor = None

            visited[node[0]][node[1]] = True
            random.shuffle(self.directions["4"])

            for offset_x, offset_y in self.directions["4"]:
                neighbor = (node[0] + offset_x, node[1] + offset_y)

                if not self.is_node_valid(neighbor, visited):
                    neighbor = None
                    continue

                break

            path.append(node)

            if neighbor:
                stack.append(neighbor)
            else:
                stack.pop()

        return path

    def get_generator(self) -> None:
        """Returns the generator for Randomized depth first search
        algorithm.

        Yields:
            None: Nothing is being yielded.
        """

        path = self.get_path()
        path_length = len(path)

        for path_index in range(1, path_length):
            previous = path[path_index - 1]
            current = path[path_index]

            self.color_node(previous, False)
            self.color_node(current, True)

            self.remove_wall(previous, current)

            yield

    def is_node_valid(self, node: Tuple[int, int], visited: List[List[bool]]) -> bool:
        """Returns the validity of using the input node in the future.

        Args:
            node (Tuple[int, int]): The node's current position.
            visited (List[List[bool]]): The list of visited nodes.

        Returns:
            bool: Returns the validity of using the input node in the future.
        """

        x, y = node

        if x < 0 or x >= MAZE_WIDTH:
            return False

        if y < 0 or y >= MAZE_HEIGHT:
            return False

        return not visited[x][y]
