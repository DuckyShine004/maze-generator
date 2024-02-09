"""This module contains application constants.

Attributes:
    CELL_COLOR (tuple): The cell's color.
    CELL_OFFSET (int): The cell offset.
    CELL_SIZE (tuple): The size of each cell.
    DIRECTIONS (TYPE): All directions types.
    FONT_COLOR (tuple): The font's color.
    FONT_SIZE (int): The font's size.
    FPS (int): The frames per second.
    GRAPH_ALGORITHM (str): The default graph traversal algorithm.
    GRAPH_DELAY (float): The animation delay.
    GRAPH_INITIAL_DELAY (float): The initial animation delay.
    HEIGHT (int): The display's height.
    HORIZONTAL_WALL_SIZE (TYPE): The length of a horizontal wall.
    MAZE_HEIGHT (int): The height of the maze.
    MAZE_WIDTH (int): The width of the maze.
    MENU (str): The path to the menu JSON file.
    SURFACE_COLOR (tuple): The color of the background.
    VERTICAL_WALL_SIZE (TYPE): The length of a vertical wall.
    WALL_COLOR (tuple): The color of each wall.
    WALL_OFFSET (int): Wall offset.
    WALL_SIZE_1 (int): Size of wall.
    WALL_SIZE_2 (int): Size of wall.
    WIDTH (int): The display's width.
    CAPTION (str): The window's title.
"""

# DISPLAY
SURFACE_COLOR = (160, 160, 160)
CAPTION = "Maze Generator"
WIDTH = 1920
HEIGHT = 1080
FPS = 60

# WALL
WALL_COLOR = (0, 0, 0)
WALL_SIZE_1 = 5
WALL_SIZE_2 = 65
WALL_OFFSET = 5
HORIZONTAL_WALL_SIZE = (WALL_SIZE_2, WALL_SIZE_1)
VERTICAL_WALL_SIZE = (WALL_SIZE_1, WALL_SIZE_2)

# CELL
CELL_COLOR = (255, 0, 0)
CELL_SIZE = (60, 60)
CELL_OFFSET = 60

# MAZE
MAZE_WIDTH = 32
MAZE_HEIGHT = 18
DIRECTIONS = {
    "2": [(0, 1), (1, 0)],
    "4": [(0, -1), (1, 0), (0, 1), (-1, 0)],
}

# GRAPH
GRAPH_INITIAL_DELAY = 0
GRAPH_DELAY = 500
GRAPH_ALGORITHM = "dfs"

# UI
MENU = "../../json/menu.json"

# FONT
FONT_COLOR = (255, 255, 255)
FONT_SIZE = 50
