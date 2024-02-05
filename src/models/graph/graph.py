from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT, CELL_OFFSET
from src.models.objects.cell import Cell


class Graph:
    def __init__(self):
        self.cells = [[None] * MAZE_HEIGHT for _ in range(MAZE_WIDTH)]

        for x in range(MAZE_WIDTH):
            is_right_most_wall = x == MAZE_WIDTH - 1

            for y in range(MAZE_HEIGHT):
                is_bottom_most_wall = y == MAZE_HEIGHT - 1
                self.cells[x][y] = Cell(
                    x * CELL_OFFSET,
                    y * CELL_OFFSET,
                    is_right_most_wall,
                    is_bottom_most_wall,
                )

    def render(self, surface):
        for row in self.cells:
            for cell in row:
                cell.render(surface)
