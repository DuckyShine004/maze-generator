import pygame

from src.constants.constants import WALL_COLOR, VERTICAL_WALL_SIZE, HORIZONTAL_WALL_SIZE


class Cell(object):
    def __init__(self, x, y):
        horizontal_wall_offset = VERTICAL_WALL_SIZE[1] - HORIZONTAL_WALL_SIZE[1]
        vertical_wall_offset = HORIZONTAL_WALL_SIZE[0] - VERTICAL_WALL_SIZE[0]

        self.walls = [
            [pygame.Rect(x, y, *HORIZONTAL_WALL_SIZE), True],
            [pygame.Rect(x + vertical_wall_offset, y, *VERTICAL_WALL_SIZE), True],
            [pygame.Rect(x, y + horizontal_wall_offset, *HORIZONTAL_WALL_SIZE), True],
            [pygame.Rect(x, y, *VERTICAL_WALL_SIZE), True],
        ]

    def render(self, surface):
        for wall, is_wall_visible in self.walls:
            # wall.center = (self.x, self.y)

            if not is_wall_visible:
                continue

            pygame.draw.rect(surface, WALL_COLOR, wall)
