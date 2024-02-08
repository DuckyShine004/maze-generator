"""This module allows for the creation of cell objects."""

from typing import List, Optional

import pygame

from src.constants.constants import (
    CELL_SIZE,
    CELL_COLOR,
    WALL_COLOR,
    VERTICAL_WALL_SIZE,
    HORIZONTAL_WALL_SIZE,
)


class Cell:
    """This class ensures that we have an easy time implementing graph algorithms for
    maze generation.

    Attributes:
        is_color_current_cell (bool): Should the current cell be colored.
        walls (list): List of walls for a cell position.
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
    """

    def __init__(
        self, x: int, y: int, is_right_most_cell: Optional[bool] = False, is_bottom_most_cell: Optional[bool] = False
    ) -> None:
        """Initializes the cell object.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            is_right_most_cell (bool): Is the cell the right most cell
            is_bottom_most_cell (bool): Is the cell the bottom most cell
        """

        self.x: int = x
        self.y: int = y

        self.walls: List[pygame.Rect] = self.get_walls(x, y, is_right_most_cell, is_bottom_most_cell)
        self.is_color_current_cell: bool = False

    def get_walls(self, x: int, y: int, is_right_most_cell: bool, is_bottom_most_cell: bool) -> List[pygame.Rect]:
        """Create and return a list of walls for the current cell position.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            is_right_most_cell (bool): Is the cell the right most cell
            is_bottom_most_cell (bool): Is the cell the bottom most cell

        Returns:
            List[pygame.Rect]: The hitbox of all walls.
        """

        horizontal_wall_offset = VERTICAL_WALL_SIZE[1] - HORIZONTAL_WALL_SIZE[1]
        vertical_wall_offset = HORIZONTAL_WALL_SIZE[0] - VERTICAL_WALL_SIZE[0]

        top_wall = [pygame.Rect(x, y, *HORIZONTAL_WALL_SIZE), True]
        right_wall = [pygame.Rect(x + vertical_wall_offset, y, *VERTICAL_WALL_SIZE), is_right_most_cell]
        bottom_wall = [pygame.Rect(x, y + horizontal_wall_offset, *HORIZONTAL_WALL_SIZE), is_bottom_most_cell]
        left_wall = [pygame.Rect(x, y, *VERTICAL_WALL_SIZE), True]

        return [top_wall, right_wall, bottom_wall, left_wall]

    def render_cell_color(self, surface: pygame.Surface) -> None:
        """Paints the current cell to predefined color.

        Args:
            surface (pygame.Surface): The surface for cells to be
            rendered on to.

        Returns:
            None: Nothing is being returned.
        """

        if not self.is_color_current_cell:
            return

        pygame.draw.rect(surface, CELL_COLOR, pygame.Rect(self.x, self.y, *CELL_SIZE))

    def render(self, surface: pygame.Surface) -> None:
        """Renders the cell object.

        Args:
            surface (pygame.Surface): The surface for cells to be
            rendered on to.
        """

        self.render_cell_color(surface)

        for wall, is_wall_visible in self.walls:
            if not is_wall_visible:
                continue

            pygame.draw.rect(surface, WALL_COLOR, wall)
