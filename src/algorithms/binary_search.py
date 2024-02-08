import random

from src.algorithms.algorithm import Algorithm
from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT


class BinarySearch(Algorithm):
    def __init__(self, graph):
        super().__init__(graph)
        self.current_neighbor = None

    def get_generator(self):
        previous = None

        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                self.handle_color_of_cells(previous, (x, y))

                is_removed = False
                index = random.randint(0, 1)
                offset_x, offset_y = self.directions["2"][index]
                neighbor = (x + offset_x, y + offset_y)
                previous = (x, y)

                if self.is_node_valid(neighbor):
                    self.handle_removal_of_wall((x, y), neighbor)
                    self.handle_color_of_current_neighbor(neighbor)
                    is_removed = True
                    yield

                if not is_removed:
                    yield

    def handle_color_of_current_neighbor(self, neighbor):
        self.current_neighbor = neighbor
        self.color_node(self.current_neighbor, True)

    def handle_color_of_cells(self, previous, current):
        self.color_node(previous, False)
        self.color_node(current, True)
        self.color_node(self.current_neighbor, False)

    def handle_removal_of_wall(self, node, neighbor):
        if neighbor[0] - node[0] == 1:
            self.remove_wall(node, neighbor, 1)

        if neighbor[1] - node[1] == 1:
            self.remove_wall(node, neighbor, 2)

    def is_node_valid(self, node):
        x, y = node

        if x < 0 or x >= MAZE_WIDTH:
            return False

        if y < 0 or y >= MAZE_HEIGHT:
            return False

        return True
