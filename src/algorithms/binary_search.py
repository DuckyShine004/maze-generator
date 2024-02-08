"""This module allows for maze generation with randomized Binary Search algorithm."""

from typing import Tuple

import random

from src.algorithms.algorithm import Algorithm

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT


class BinarySearch(Algorithm):
    """This class initializes the Binary object. A maze, believe it or not,
    can be generated with randomized Binary Search algorithm.

    Attributes:
        current_neighbor (tuple): The current neighbor's position.
    """

    def __init__(self, graph) -> None:
        """Initializes the Binary Search algorithm object.

        Args:
            graph (Graph): The singleton graph object.
        """

        super().__init__(graph)
        self.current_neighbor: Tuple[int, int] = None

    def get_generator(self) -> None:
        """Returns the generator for the Binary Search algorithm.

        Yields:
            None: Nothing is yielded.
        """

        previous = None

        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                self.handle_color_of_cells(previous, (x, y))

                is_removed = False
                index = random.randint(0, 1)
                offset_x, offset_y = self.directions["2"][index]
                neighbor = (x + offset_x, y + offset_y)
                previous = (x, y)

                if self.is_node_valid(neighbor):
                    self.remove_wall((x, y), neighbor)
                    self.handle_color_of_current_neighbor(neighbor)
                    is_removed = True
                    yield

                if not is_removed:
                    yield

    def handle_color_of_current_neighbor(self, neighbor: Tuple[int, int]) -> None:
        """Color in the current neighbor node.

        Args:
            neighbor (Tuple[int, int]): The neighbor's position.
        """

        self.current_neighbor = neighbor
        self.color_node(self.current_neighbor, True)

    def handle_color_of_cells(self, previous: Tuple[int, int], current: Tuple[int, int]) -> None:
        """Handle coloring the previous node and the current node.

        Args:
            previous (Tuple[int, int]): The previous node's position.
            current (Tuple[int, int]): The node's current position.
        """

        self.color_node(previous, False)
        self.color_node(current, True)
        self.color_node(self.current_neighbor, False)

    def is_node_valid(self, node: Tuple[int, int]) -> bool:
        """Returns the validity of using the input node in the future.

        Args:
            node (Tuple[int, int]): The node's current position.

        Returns:
            bool: Returns the validity of using the input node in the future.
        """

        x, y = node

        if x < 0 or x >= MAZE_WIDTH:
            return False

        if y < 0 or y >= MAZE_HEIGHT:
            return False

        return True
