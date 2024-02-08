"""This module allows for the creation of visual components."""

from typing import Dict

import pygame

from src.utilities.utility import Utility


class Visual:
    """This class initializes a visual component. A visual component
    is any user interface element that requires image rendering.

    Attributes:
        image (pygame.Surface): The current image.
        images (dict): List of sprite images.
        rect (pygame.Rect): The hitbox of the image.
    """

    def __init__(self, **kwargs) -> None:
        """Initializes the visual component object.

        Args:
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        self.images: Dict[str, pygame.Surface] = Utility.get_images(kwargs["images"])
        self.image: pygame.Surface = self.images["default"]
        self.rect: pygame.Rect = self.image.get_rect(topleft=kwargs["start"])

    def render(self, surface: pygame.Surface) -> None:
        """Renders the visual component.

        Args:
            surface (pygame.Surface): The surface for the component to be
            rendered on to.
        """

        surface.blit(self.image, self.rect)
