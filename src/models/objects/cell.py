import pygame

from src.constants.constants import (
    CELL_SIZE,
    CELL_COLOR,
    WALL_COLOR,
    VERTICAL_WALL_SIZE,
    HORIZONTAL_WALL_SIZE,
)


class Cell(object):
    def __init__(self, x, y, is_right_most_wall=False, is_bottom_most_wall=False):
        self.x = x
        self.y = y

        self.walls = self.get_walls(x, y, is_right_most_wall, is_bottom_most_wall)
        self.is_color_current_cell = False

    def get_walls(self, x, y, is_right_most_wall, is_bottom_most_wall):
        horizontal_wall_offset = VERTICAL_WALL_SIZE[1] - HORIZONTAL_WALL_SIZE[1]
        vertical_wall_offset = HORIZONTAL_WALL_SIZE[0] - VERTICAL_WALL_SIZE[0]

        top_wall = [pygame.Rect(x, y, *HORIZONTAL_WALL_SIZE), True]
        right_wall = [pygame.Rect(x + vertical_wall_offset, y, *VERTICAL_WALL_SIZE), is_right_most_wall]
        bottom_wall = [pygame.Rect(x, y + horizontal_wall_offset, *HORIZONTAL_WALL_SIZE), is_bottom_most_wall]
        left_wall = [pygame.Rect(x, y, *VERTICAL_WALL_SIZE), True]

        return [top_wall, right_wall, bottom_wall, left_wall]

    def render_cell_color(self, surface):
        if not self.is_color_current_cell:
            return

        pygame.draw.rect(surface, CELL_COLOR, pygame.Rect(self.x, self.y, *CELL_SIZE))

    def render(self, surface):
        self.render_cell_color(surface)

        for wall, is_wall_visible in self.walls:
            if not is_wall_visible:
                continue

            pygame.draw.rect(surface, WALL_COLOR, wall)
