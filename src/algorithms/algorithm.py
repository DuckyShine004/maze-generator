from src.constants.constants import DIRECTIONS


class Algorithm:
    def __init__(self, graph):
        self.graph = graph
        self.directions = dict(DIRECTIONS)

    def color_node(self, node, is_color):
        if not node:
            return

        self.graph.cells[node[0]][node[1]].is_color_current_cell = is_color

    def remove_wall(self, node, neighbor, direction):
        match direction:
            case 0:
                self.graph.cells[node[0]][node[1]].walls[0][1] = False
            case 1:
                self.graph.cells[neighbor[0]][neighbor[1]].walls[3][1] = False
            case 2:
                self.graph.cells[neighbor[0]][neighbor[1]].walls[0][1] = False
            case 3:
                self.graph.cells[node[0]][node[1]].walls[3][1] = False
