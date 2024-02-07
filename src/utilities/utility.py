import os
import json
import random
import pygame

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT


class Utility:
    @staticmethod
    def get_random_position():
        x = random.randint(0, MAZE_WIDTH - 1)
        y = random.randint(0, MAZE_HEIGHT - 1)

        return (x, y)

    @staticmethod
    def get_json_data(path):
        directory_path = os.path.dirname(os.path.realpath(__file__))
        absolute_path = os.path.join(directory_path, path)

        with open(absolute_path, "r") as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_images(paths):
        images = {}

        for key, path in paths.items():
            images[key] = pygame.image.load(path)

        return images

    @staticmethod
    def clamp(value, _min, _max):
        if value < _min:
            return _min

        if value > _max:
            return _max

        return value
