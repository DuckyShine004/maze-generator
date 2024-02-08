from src.constants.constants import DIRECTIONS


class Algorithm:
    def __init__(self, graph):
        self.graph = graph
        self.directions = dict(DIRECTIONS)

    def color_node(self, node, is_color):
        if not node:
            return

        self.graph.cells[node[0]][node[1]].is_color_current_cell = is_color

    def get_direction(self, node, neighbor):
        if neighbor[0] - node[0] == 1:
            return 1

        if neighbor[0] - node[0] == -1:
            return 3

        if neighbor[1] - node[1] == 1:
            return 2

        if neighbor[1] - node[1] == -1:
            return 0

        return -1

    def remove_wall(self, node, neighbor):
        direction = self.get_direction(node, neighbor)

        match direction:
            case 0:
                self.graph.cells[node[0]][node[1]].walls[0][1] = False
            case 1:
                self.graph.cells[neighbor[0]][neighbor[1]].walls[3][1] = False
            case 2:
                self.graph.cells[neighbor[0]][neighbor[1]].walls[0][1] = False
            case 3:
                self.graph.cells[node[0]][node[1]].walls[3][1] = False
            case _:
                pass
