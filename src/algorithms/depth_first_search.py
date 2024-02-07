import random

from collections import deque

from src.utilities.utility import Utility

from src.algorithms.algorithm import Algorithm

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT


class DepthFirstSearch(Algorithm):
    def __init__(self, graph):
        super().__init__(graph)
        self.initialize()

    def initialize(self):
        visited = [[False] * MAZE_HEIGHT for _ in range(MAZE_WIDTH)]

        start = Utility.get_random_position()
        stack = deque([start])

        while stack:
            node = stack[-1]
            neighbor = None

            visited[node[0]][node[1]] = True
            random.shuffle(self.directions_4)

            for offset_x, offset_y in self.directions_4:
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

    def is_node_valid(self, node, visited):
        x, y = node

        if x < 0 or x >= MAZE_WIDTH:
            return False

        if y < 0 or y >= MAZE_HEIGHT:
            return False

        return not visited[x][y]
