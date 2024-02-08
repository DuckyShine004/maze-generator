"""This module allows for maze generation with randomized Kruskal's algorithm."""

from typing import List, Tuple

import random

from src.algorithms.algorithm import Algorithm
from src.algorithms.union_find import UnionFind

from src.constants.constants import MAZE_HEIGHT, MAZE_WIDTH


class Kruskal(Algorithm):
    """This class initializes the Kruskal object. A maze, believe it or not,
    can be generated with randomized Kruskal's algorithm.

    Attributes:
        current_neighbor (tuple): The current neighbor's position.
        nodes (list[tuple]): List of nodes.
        union_find (UnionFind): The union find datastructure.
    """

    def __init__(self, graph) -> None:
        """Initializes the Kruskal's algorithm object.

        Args:
            graph (Graph): The singleton graph object.
        """

        super().__init__(graph)

        self.nodes: List[Tuple[int, int]] = [(x, y) for x in range(MAZE_WIDTH) for y in range(MAZE_HEIGHT)]
        self.union_find: UnionFind = UnionFind(MAZE_WIDTH * MAZE_HEIGHT)
        self.current_neighbor: Tuple[int, int] = None

        random.shuffle(self.nodes)

    def get_generator(self) -> None:
        """Returns the generator for Kruskal's algorithm.

        Yields:
            None: Nothing is yielded.
        """

        previous = None

        while self.nodes:
            node = self.nodes.pop()
            neighbor = None

            self.handle_color_of_cells(previous, node)

            random.shuffle(self.directions["4"])
            previous = node

            for offset_x, offset_y in self.directions["4"]:
                neighbor = (node[0] + offset_x, node[1] + offset_y)

                if not self.is_node_valid(node, neighbor):
                    neighbor = None
                    continue

                break

            if neighbor:
                self.remove_wall(node, neighbor)
                self.handle_color_of_current_neighbor(neighbor)

            yield

        self.uncolor_remaining_cells(previous)

    def get_index(self, node: Tuple[int, int]) -> int:
        """Calculates the one-dimensional index from the input two-
        dimensional index (position).

        Args:
            node (Tuple[int, int]): The node's current position.

        Returns:
            int: Returns a one-dimensional index, given a two-dimensional
            index.
        """

        x, y = node

        return x + (y * MAZE_WIDTH)

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

    def is_node_valid(self, node: Tuple[int, int], neighbor: Tuple[int, int]) -> bool:
        """Returns the validity of using the input node in the future.

        Args:
            node (Tuple[int, int]): The node's current position.
            neighbor (Tuple[int, int]): he neighbor's position.

        Returns:
            bool: Returns the validity of using the input node in the future.
        """

        x, y = neighbor

        if x < 0 or x >= MAZE_WIDTH:
            return False

        if y < 0 or y >= MAZE_HEIGHT:
            return False

        if not self.is_union_of_nodes_valid(node, neighbor):
            return False

        return True

    def is_union_of_nodes_valid(self, node: Tuple[int, int], neighbor: Tuple[int, int]) -> bool:
        """Returns the validity of merging the current node and
            the neighbor node.

        Args:
            node (Tuple[int, int]): The current node's position.
            neighbor (Tuple[int, int]): The neighbor's position.

        Returns:
            bool: Returns the validity of merging the current node and
            the neighbor node.
        """

        node_index = self.get_index(node)
        neighbor_index = self.get_index(neighbor)

        return self.union_find.union(node_index, neighbor_index)
