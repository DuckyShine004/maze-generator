import pygame

from src.constants.constants import (
    WALL_COLOR,
    VERTICAL_WALL_SIZE,
    HORIZONTAL_WALL_SIZE,
)


class Cell(object):
    def __init__(self, x, y, is_right_most_wall=False, is_bottom_most_wall=False):
        self.x = x
        self.y = y
        self.is_current_cell = False

        horizontal_wall_offset = VERTICAL_WALL_SIZE[1] - HORIZONTAL_WALL_SIZE[1]
        vertical_wall_offset = HORIZONTAL_WALL_SIZE[0] - VERTICAL_WALL_SIZE[0]

        self.cells = [
            [pygame.Rect(x, y, *HORIZONTAL_WALL_SIZE), True],
            [
                pygame.Rect(x + vertical_wall_offset, y, *VERTICAL_WALL_SIZE),
                is_right_most_wall,
            ],
            [
                pygame.Rect(x, y + horizontal_wall_offset, *HORIZONTAL_WALL_SIZE),
                is_bottom_most_wall,
            ],
            [pygame.Rect(x, y, *VERTICAL_WALL_SIZE), True],
        ]

    def render(self, surface):
        if self.is_current_cell:
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.x, self.y, 60, 60))

        for wall, is_wall_visible in self.walls:
            if not is_wall_visible:
                continue

            pygame.draw.rect(surface, WALL_COLOR, wall)
