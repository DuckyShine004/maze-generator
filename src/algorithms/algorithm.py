"""This module allows for generation of a maze."""

from typing import TYPE_CHECKING, List, Dict, Tuple

from src.constants.constants import DIRECTIONS

if TYPE_CHECKING:
    from src.models.graph.graph import Graph


class Algorithm:
    """This class initializes the algorithm component. An algorithm is
    any class that involved generating a maze.

    Attributes:
        directions (dict): Dictionary of directions.
        graph (Graph): The singleton graph object.
    """

    def __init__(self, graph: "Graph") -> None:
        """Initialize the algorithm object.

        Args:
            graph (Graph): The singleton graph object.
        """

        self.graph: "Graph" = graph
        self.directions: Dict[str, List[Tuple[int, int]]] = dict(DIRECTIONS)

    def color_node(self, node: Tuple[int, int], is_color: bool) -> None:
        """Color/uncolor the node at the input node's position.

        Args:
            node (Tuple[int, int]): The current node's position.
            is_color (bool): Should we color the input node.

        Returns:
            None: Nothing is being returned.
        """

        if not node:
            return

        self.graph.cells[node[0]][node[1]].is_color_current_cell = is_color

    def get_direction(self, node: Tuple[int, int], neighbor: Tuple[int, int]) -> int:
        """Get the direction between two nodes. In this case, between the
        current node and the neighbor node.

        Args:
            node (Tuple[int, int]): The current position of the node.
            neighbor (Tuple[int, int]): The neighbor's position.

        Returns:
            int: Return the direction.
        """

        if neighbor[0] - node[0] == 1:
            return 1

        if neighbor[0] - node[0] == -1:
            return 3

        if neighbor[1] - node[1] == 1:
            return 2

        if neighbor[1] - node[1] == -1:
            return 0

        return -1

    def remove_wall(self, node: Tuple[int, int], neighbor: Tuple[int, int]) -> None:
        """Remove the wall between the node and the neighbor.

        Args:
            node (Tuple[int, int]): The current position of the node.
            neighbor (Tuple[int, int]): The neighbor's position.
        """

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
