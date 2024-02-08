import random

from collections import deque

from src.algorithms.algorithm import Algorithm

from src.utilities.utility import Utility

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT


class DepthFirstSearch(Algorithm):
    def __init__(self, graph):
        super().__init__(graph)

        self.path = deque()

        self.initialize()

    def initialize(self):
        visited = [[False] * MAZE_HEIGHT for _ in range(MAZE_WIDTH)]

        start = Utility.get_random_position()
        stack = deque([start])

        while stack:
            node = stack[-1]
            neighbor = None

            visited[node[0]][node[1]] = True
            random.shuffle(self.directions["4"])

            for offset_x, offset_y in self.directions["4"]:
                neighbor = (node[0] + offset_x, node[1] + offset_y)

                if not self.is_node_valid(neighbor, visited):
                    neighbor = None
                    continue

                break

            self.path.append(node)

            if neighbor:
                stack.append(neighbor)
            else:
                stack.pop()

    def get_generator(self):
        path_length = len(self.path)

        for path_index in range(1, path_length):
            previous = self.path[path_index - 1]
            current = self.path[path_index]

            self.color_node(previous, False)
            self.color_node(current, True)

            self.remove_wall(previous, current)

            yield

    def is_node_valid(self, node, visited):
        x, y = node

        if x < 0 or x >= MAZE_WIDTH:
            return False

        if y < 0 or y >= MAZE_HEIGHT:
            return False

        return not visited[x][y]
