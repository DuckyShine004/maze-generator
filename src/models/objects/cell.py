import pygame

from src.constants.constants import WALL_COLOR


class Cell(object):
    def __init__(self, x, y):
        self.walls = [
            [pygame.Rect(x, y, 30, 30), True],
            [pygame.Rect(x, y, 30, 30), True],
            [pygame.Rect(x, y, 30, 30), True],
            [pygame.Rect(x, y, 30, 30), True],
        ]

    def render(self, surface):
        for wall, is_wall_visible in self.walls:
            if not is_wall_visible:
                continue

            pygame.draw.rect(surface, WALL_COLOR, wall)
