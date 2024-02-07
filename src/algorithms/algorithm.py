from src.constants.constants import DIRECTIONS


class Algorithm:
    def __init__(self, graph):
        self.graph = graph
        self.path = []
        self.directions_4 = list(DIRECTIONS)

    def get_generator(self):
        path_length = len(self.path)

        for path_index in range(1, path_length):
            previous = self.path[path_index - 1]
            current = self.path[path_index]

            self.graph.cells[previous[0]][previous[1]].is_head_at_current_cell = False
            self.graph.cells[current[0]][current[1]].is_head_at_current_cell = True

            if current[0] - previous[0] > 0:
                self.remove_wall(previous, current, 1)

            if current[0] - previous[0] < 0:
                self.remove_wall(previous, current, 3)

            if current[1] - previous[1] > 0:
                self.remove_wall(previous, current, 2)

            if current[1] - previous[1] < 0:
                self.remove_wall(previous, current, 0)

            yield

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
