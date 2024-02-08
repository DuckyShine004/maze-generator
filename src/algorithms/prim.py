"""This module allows for maze generation with randomized Prim's algorithm."""

from typing import TYPE_CHECKING, List, Tuple

import random

from src.algorithms.algorithm import Algorithm

from src.utilities.utility import Utility

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT

if TYPE_CHECKING:
    from src.models.graph.graph import Graph


class Prim(Algorithm):
    """This class initializes the Prim object. A maze, believe it or not,
    can be generated with randomized Prim's algorithm.

    Attributes:
        current_neighbor (tuple): The current neighbor's position.
    """

    def __init__(self, graph: "Graph") -> None:
        """Initializes the Prim's algorithm object.

        Args:
            graph (Graph): The singleton graph object.
        """

        super().__init__(graph)
        self.current_neighbor: Tuple[int, int] = None

    def get_generator(self) -> None:
        """Returns the generator for Prim's algorithm.

        Yields:
            None: Nothing is yielded.
        """

        visited = [[False] * MAZE_HEIGHT for _ in range(MAZE_WIDTH)]

        start = Utility.get_random_position()
        frontier = [start]

        previous = None

        while frontier:
            index = random.randint(0, len(frontier) - 1)
            node = frontier.pop(index)
            neighbor = None

            if visited[node[0]][node[1]]:
                yield
                continue

            visited[node[0]][node[1]] = True

            self.handle_color_of_cells(previous, node)

            random.shuffle(self.directions["4"])
            previous = node

            for offset_x, offset_y in self.directions["4"]:
                temporary_node = (node[0] + offset_x, node[1] + offset_y)

                if not self.is_node_valid(temporary_node, visited):
                    continue

                frontier.append(temporary_node)

                if neighbor:
                    continue

                neighbor = temporary_node

            if neighbor:
                self.remove_wall(node, neighbor)
                self.handle_color_of_current_neighbor(neighbor)

            yield

        self.uncolor_remaining_cells(previous)

    def handle_color_of_cells(self, previous: Tuple[int, int], current: Tuple[int, int]) -> None:
        """Handle coloring the previous node and the current node.

        Args:
            previous (Tuple[int, int]): The previous node's position.
            current (Tuple[int, int]): The node's current position.
        """

        self.color_node(previous, False)
        self.color_node(current, True)
        self.color_node(self.current_neighbor, False)

    def handle_color_of_current_neighbor(self, neighbor: Tuple[int, int]) -> None:
        """Color in the current neighbor node.

        Args:
            neighbor (Tuple[int, int]): The neighbor's position.
        """

        self.current_neighbor = neighbor
        self.color_node(self.current_neighbor, True)

    def uncolor_remaining_cells(self, node: Tuple[int, int]) -> None:
        """Uncolor the remaining nodes.

        Args:
            node (Tuple[int, int]): The node's current position.
        """

        self.color_node(node, False)
        self.color_node(self.current_neighbor, False)

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
