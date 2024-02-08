"""This module initializes user interface components."""

from typing import TYPE_CHECKING

import pygame

from src.ui.sub.moveable import Moveable
from src.ui.sub.visual import Visual
from src.ui.sub.text import Text

if TYPE_CHECKING:
    from src.app.app import App


class Element:
    """This class initializes the element object. An element is a component
    of the user interface.

    Attributes:
        id (str): The id of the element.
        moveable (Moveable): Moveable instance.
        text (Text): Text instance.
        type (str): The type of element.
        visual (Visual): Visual instance.
        z_buffer (int): Defines which elements are rendered first.
    """

    def __init__(self, app: "App", **kwargs) -> None:
        """Initializes the element object.

        Args:
            app (App): Singleton instance of app.
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        self.app: "App" = app

        self.id: str = kwargs["id"]
        self.type: str = kwargs["type"]
        self.z_buffer: int = kwargs["z-buffer"]

        self.moveable: "Moveable" = Moveable(self, **kwargs)
        self.visual: "Visual" = Visual(**kwargs)
        self.text: "Text" = Text(self, **kwargs)

    def is_hovered(self) -> bool:
        """Returns a boolean value based on whether the current
        element is in contact with the cursor.

        Returns:
            bool: Is the cursor in contact with the element.
        """

        if self.type == "default":
            return False

        return self.visual.rect.collidepoint(pygame.mouse.get_pos())

    def on_move(self) -> None:
        """Handle the movement of the element."""

        self.moveable.on_move()

    def on_slide(self) -> None:
        """Handles the sliding movement of the element."""

        self.moveable.on_slide()
        self.text.on_slide()

    def render(self, surface: pygame.Surface) -> None:
        """Renders the current element.

        Args:
            surface (pygame.Surface): The surface for elements to be rendered on to.
        """

        self.visual.render(surface)
        self.text.render(surface)
