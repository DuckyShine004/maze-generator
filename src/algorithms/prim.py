import random

from src.algorithms.algorithm import Algorithm

from src.utilities.utility import Utility

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT


class Prim(Algorithm):
    def __init__(self, graph):
        super().__init__(graph)
        self.current_neighbor = None

    def get_generator(self):
        visited = [[False] * MAZE_HEIGHT for _ in range(MAZE_WIDTH)]

        start = Utility.get_random_position()
        frontier = [start]

        previous = None

        while frontier:
            index = random.randint(0, len(frontier) - 1)
            node = frontier.pop(index)
            neighbor = None

            if visited[node[0]][node[1]]:
                yield
                continue

            visited[node[0]][node[1]] = True

            self.handle_color_of_cells(previous, node)

            random.shuffle(self.directions["4"])
            previous = node

            for offset_x, offset_y in self.directions["4"]:
                temporary_node = (node[0] + offset_x, node[1] + offset_y)

                if not self.is_node_valid(temporary_node, visited):
                    continue

                frontier.append(temporary_node)

                if neighbor:
                    continue

                neighbor = temporary_node

            if neighbor:
                self.remove_wall(node, neighbor)
                self.handle_color_of_current_neighbor(neighbor)

            yield

        self.uncolor_remaining_cells(previous)

    def handle_color_of_cells(self, previous, current):
        self.color_node(previous, False)
        self.color_node(current, True)
        self.color_node(self.current_neighbor, False)

    def handle_color_of_current_neighbor(self, neighbor):
        self.current_neighbor = neighbor
        self.color_node(self.current_neighbor, True)

    def uncolor_remaining_cells(self, node):
        self.color_node(node, False)
        self.color_node(self.current_neighbor, False)

    def is_node_valid(self, node, visited):
        x, y = node

        if x < 0 or x >= MAZE_WIDTH:
            return False

        if y < 0 or y >= MAZE_HEIGHT:
            return False

        return not visited[x][y]
