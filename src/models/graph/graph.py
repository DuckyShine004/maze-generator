"""This module allows the user to create a maze."""

from typing import List, Iterator

import pygame

from src.models.objects.cell import Cell

from src.algorithms.depth_first_search import DepthFirstSearch
from src.algorithms.binary_search import BinarySearch
from src.algorithms.kruskal import Kruskal
from src.algorithms.prim import Prim

from src.constants.constants import (
    MAZE_WIDTH,
    MAZE_HEIGHT,
    CELL_OFFSET,
    GRAPH_INITIAL_DELAY,
    GRAPH_ALGORITHM,
)


class Graph:
    """This class initializes the graph. A graph datastructure is needed
    to store essential fields and methods for generating a maze.

    Attributes:
        algorithm (str): The current algorithm type.
        cells (Cell): Instance of cell object.
        delay (int): The delay between each animation frame.
        generator (Iterator[None]): The path generator for the graph.
        previous_time (int): The previous frame for animation.
    """

    def __init__(self) -> None:
        """Initializes the graph object."""

        self.cells: List[Cell] = [
            [
                Cell(
                    x * CELL_OFFSET,
                    y * CELL_OFFSET,
                    x == MAZE_WIDTH - 1,
                    y == MAZE_HEIGHT - 1,
                )
                for y in range(MAZE_HEIGHT)
            ]
            for x in range(MAZE_WIDTH)
        ]

        self.generator: Iterator[None] = None
        self.previous_time: int = None
        self.delay: int = GRAPH_INITIAL_DELAY
        self.algorithm: str = GRAPH_ALGORITHM

    def reset(self) -> None:
        """Resets the graph. Essentially resets attributes to initial
        state.
        """

        self.cells = [
            [
                Cell(
                    x * CELL_OFFSET,
                    y * CELL_OFFSET,
                    x == MAZE_WIDTH - 1,
                    y == MAZE_HEIGHT - 1,
                )
                for y in range(MAZE_HEIGHT)
            ]
            for x in range(MAZE_WIDTH)
        ]

        self.generator = None
        self.previous_time = None

    def get_next_path(self, time: int) -> None:
        """Get the next path from the generator.

        Args:
            time (int): The current frame.

        Returns:
            None: Nothing is returned.
        """

        if not self.generator:
            return

        print(type(self.generator))

        try:
            next(self.generator)
            self.previous_time = time
        except StopIteration:
            self.generator = None
            self.previous_time = None

    def update(self) -> None:
        """Updates the graph."""

        time = pygame.time.get_ticks()
        delta_time = None

        if self.previous_time is not None:
            delta_time = time - self.previous_time

        if delta_time is None or delta_time >= self.delay:
            self.get_next_path(time)

    def set_algorithm(self, algorithm: str) -> None:
        """Set the algorithm picked.

        Args:
            algorithm (str): The type of algorithm.
        """

        self.algorithm = algorithm

    def generate(self) -> None:
        """Generate the graph based on the current algorithm."""

        self.reset()
        self.set_generator()

    def set_generator(self) -> None:
        """When the user selects an algorithm, we need to set it and
        create a generator for that algorithm.
        """

        algorithm = DepthFirstSearch(self)

        match self.algorithm:
            case "dfs":
                algorithm = DepthFirstSearch(self)
            case "binary":
                algorithm = BinarySearch(self)
            case "kruskal":
                algorithm = Kruskal(self)
            case "prim":
                algorithm = Prim(self)

        self.generator = algorithm.get_generator()

    def render(self, surface: pygame.Surface) -> None:
        """Renders all components used to create the graph.

        Args:
            surface (pygame.Surface): The surface for graph components
            to be rendered on to.
        """

        for row in self.cells:
            for cell in row:
                cell.render(surface)
