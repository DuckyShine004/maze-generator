import random
from src.algorithms.algorithm import Algorithm
from src.algorithms.union_find import UnionFind

from src.constants.constants import MAZE_HEIGHT, MAZE_WIDTH


class Kruskal(Algorithm):
    def __init__(self, graph):
        super().__init__(graph)

        self.nodes = [(x, y) for x in range(MAZE_WIDTH) for y in range(MAZE_HEIGHT)]
        random.shuffle(self.nodes)

        self.union_find = UnionFind(MAZE_WIDTH * MAZE_HEIGHT)

    def get_generator(self):
        while self.nodes:
            node = self.nodes.pop()
            neighbor = None

            random.shuffle(self.directions["4"])

            for offset_x, offset_y in self.directions["4"]:
                neighbor = (node[0] + offset_x, node[1] + offset_y)

                if not self.is_node_valid(node, neighbor):
                    neighbor = None
                    continue

                break

            if neighbor:
                self.remove_wall(node, neighbor)

    def get_index(self, node):
        x, y = node

        return x + (y * MAZE_WIDTH)

    def is_node_valid(self, node, neighbor):
        x, y = neighbor

        if x < 0 or x >= MAZE_WIDTH:
            return False

        if y < 0 or y >= MAZE_HEIGHT:
            return False

        if not self.is_union_of_nodes_valid(node, neighbor):
            return False

        return True

    def is_union_of_nodes_valid(self, node, neighbor):
        node_index = self.get_index(node)
        neighbor_index = self.get_index(neighbor)

        return self.union_find.union(node_index, neighbor_index)
