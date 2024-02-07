import random
import pygame

from collections import deque
from src.utilities.utility import Utility

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT, CELL_OFFSET, DIRECTIONS
from src.models.objects.cell import Cell


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
        self.delay = 10
        self.algorithm = "dfs"

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

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.generator and (
            self.previous_time is None
            or (current_time - self.previous_time >= self.delay)
        ):
            try:
                next(self.generator)
                self.previous_time = current_time
            except StopIteration:
                self.generator = None
                self.previous_time = None

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def generate(self):
        self.reset()
        path = None

        match self.algorithm:
            case "dfs":
                path = self.dfs()
            case "binary":
                path = self.binary()

        self.generator = self.get_generator(path)

    def get_generator(self, path):
        for i in range(1, len(path)):
            u = path[i - 1]
            v = path[i]

            ux, uy = u
            vx, vy = v

            self.cells[ux][uy].is_current_cell = False
            self.cells[vx][vy].is_current_cell = True

            if vx - ux > 0:
                self.remove_wall(u, v, 1)

            if vx - ux < 0:
                self.remove_wall(u, v, 3)

            if vy - uy > 0:
                self.remove_wall(u, v, 2)

            if vy - uy < 0:
                self.remove_wall(u, v, 0)

            yield

    def dfs(self):
        directions = DIRECTIONS.copy()
        start_cell = Utility.get_random_position()
        visited = [[False] * MAZE_HEIGHT for _ in range(MAZE_WIDTH)]
        stack = deque([start_cell])
        path = deque()

        while stack:
            u = stack[-1]
            x, y = u

            v = None

            visited[x][y] = True
            random.shuffle(directions)

            for dx, dy in directions:
                v = (x + dx, y + dy)

                if not self.is_valid(v, visited):
                    v = None
                    continue

                break

            path.append(u)

            if v:
                stack.append(v)
            else:
                stack.pop()

        return path

    def binary(self):
        path = deque()

        for x in range(MAZE_WIDTH):
            for y in range(MAZE_HEIGHT):
                ...

        return path

    def is_valid(self, node, visited):
        x, y = node

        if x < 0 or x >= MAZE_WIDTH:
            return False

        if y < 0 or y >= MAZE_HEIGHT:
            return False

        return not visited[x][y]

    def remove_wall(self, u, v, direction):
        ux, uy = u
        vx, vy = v

        match direction:
            case 0:
                self.cells[ux][uy].walls[0][1] = False
            case 1:
                self.cells[vx][vy].walls[3][1] = False
            case 2:
                self.cells[vx][vy].walls[0][1] = False
            case 3:
                self.cells[ux][uy].walls[3][1] = False
            case _:
                pass

    def render(self, surface):
        for row in self.cells:
            for cell in row:
                cell.render(surface)
