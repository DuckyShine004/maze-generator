import pygame

from src.models.objects.cell import Cell

from src.algorithms.depth_first_search import DepthFirstSearch
from src.algorithms.binary_search import BinarySearch
from src.algorithms.kruskal import Kruskal


from src.constants.constants import (
    MAZE_WIDTH,
    MAZE_HEIGHT,
    CELL_OFFSET,
    GRAPH_DELAY,
    GRAPH_ALGORITHM,
)


class Graph:
    def __init__(self):
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
        self.delay = GRAPH_DELAY
        self.algorithm = GRAPH_ALGORITHM

    def reset(self):
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

    def get_next_path(self, time):
        if not self.generator:
            return

        try:
            next(self.generator)
            self.previous_time = time
        except StopIteration:
            self.generator = None
            self.previous_time = None

    def update(self):
        time = pygame.time.get_ticks()
        delta_time = None

        if self.previous_time is not None:
            delta_time = time - self.previous_time

        if delta_time is None or delta_time >= self.delay:
            self.get_next_path(time)

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def generate(self):
        self.reset()
        self.set_generator()

    def set_generator(self):
        algorithm = DepthFirstSearch(self)

        match self.algorithm:
            case "dfs":
                algorithm = DepthFirstSearch(self)
            case "binary":
                algorithm = BinarySearch(self)
            case "kruskal":
                algorithm = Kruskal(self)

        self.generator = algorithm.get_generator()

    def render(self, surface):
        for row in self.cells:
            for cell in row:
                cell.render(surface)
