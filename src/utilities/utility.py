import random

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT


class Utility:
    @staticmethod
    def get_random_position():
        x = random.randint(0, MAZE_WIDTH - 1)
        y = random.randint(0, MAZE_HEIGHT - 1)

        return (x, y)
