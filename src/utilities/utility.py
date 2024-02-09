"""The module contains methods that are beneficial for every other module."""

from typing import Dict, Tuple, Any

import os
import json
import random
import pygame

from src.constants.constants import MAZE_WIDTH, MAZE_HEIGHT


class Utility:
    """The Utility class contains useful methods which other modules might need."""

    @staticmethod
    def get_random_position() -> Tuple[int, int]:
        """Returns a random cell position.

        Returns:
            Tuple[int, int]: random cell position.
        """

        x = random.randint(0, MAZE_WIDTH - 1)
        y = random.randint(0, MAZE_HEIGHT - 1)

        return (x, y)

    @staticmethod
    def get_json_data(path: str) -> Any:
        """Returns the JSON data.

        Args:
            path (str): The path to the JSON file.

        Returns:
            Any: JSON data.
        """

        directory_path = os.path.dirname(os.path.realpath(__file__))
        absolute_path = os.path.join(directory_path, path)

        with open(absolute_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    @staticmethod
    def get_images(paths: Dict[str, str]) -> Dict[str, pygame.Surface]:
        """Returns a list of pygame loaded images.

        Args:
            paths (Dict[str, str]): A list of paths.

        Returns:
            Dict[str, pygame.Surface]: List of pygame images.
        """

        images = {}

        for key, path in paths.items():
            images[key] = pygame.image.load(path)

        return images

    @staticmethod
    def clamp(value: int, _min: int, _max: int) -> int:
        """Clamps the input value between _min and _max.

        Args:
            value (float): The value to be clamped.
            _min (float): The lower bound.
            _max (float): The upper bound.

        Returns:
            float: The clamped value.
        """

        if value < _min:
            return _min

        if value > _max:
            return _max

        return value
