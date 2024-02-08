import random

from src.algorithms.algorithm import Algorithm
from src.algorithms.union_find import UnionFind

from src.constants.constants import MAZE_HEIGHT, MAZE_WIDTH


class Kruskal(Algorithm):
    def __init__(self, graph):
        super().__init__(graph)

        self.nodes = [(x, y) for x in range(MAZE_WIDTH) for y in range(MAZE_HEIGHT)]
        self.union_find = UnionFind(MAZE_WIDTH * MAZE_HEIGHT)
        self.current_neighbor = None

        random.shuffle(self.nodes)

    def get_generator(self):
        previous = None

        while self.nodes:
            node = self.nodes.pop()
            neighbor = None

            self.handle_color_of_cells(previous, node)

            random.shuffle(self.directions["4"])
            previous = node

            for offset_x, offset_y in self.directions["4"]:
                neighbor = (node[0] + offset_x, node[1] + offset_y)

                if not self.is_node_valid(node, neighbor):
                    neighbor = None
                    continue

                break

            if neighbor:
                self.remove_wall(node, neighbor)
                self.handle_color_of_current_neighbor(neighbor)

            yield

        self.uncolor_remaining_cells(previous)

    def get_index(self, node):
        x, y = node

        return x + (y * MAZE_WIDTH)

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
