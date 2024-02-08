"""This module allows for the creation of text components."""

from typing import TYPE_CHECKING, Tuple

import pygame

from src.constants.constants import FONT_COLOR, FONT_SIZE

if TYPE_CHECKING:
    from src.ui.element import Element


class Text:
    """This class initializes the text component. A text component is
    any component that requires text rendering.

    Attributes:
        element (Element): The element that requires text rendering.
        font (pygame.Font): The type of font.
        rect (pygame.Font): The hitbox of the text object.
        surface (pygame.Surface): The text's surface for the text
        component to be rendered on to.
        text (str): The message/text.
    """

    def __init__(self, element: "Element", **kwargs) -> None:
        """Initializes the text component object.

        Args:
            element (Element): Instance of user interface element.
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        self.element: "Element" = element

        self.text: str = kwargs.get("text", "")

        font_path: str = kwargs.get("font_path", None)
        font_size: int = kwargs.get("font_size", FONT_SIZE)
        font_color: Tuple[int, int, int] = kwargs.get("font_color", FONT_COLOR)

        self.font: pygame.Font = pygame.font.Font(font_path, font_size)
        self.surface: pygame.Surface = self.font.render(self.text, True, font_color)
        self.rect: pygame.Rect = self.surface.get_rect(center=self.element.visual.rect.center)

    def on_slide(self) -> None:
        """Handles the sliding movement of the text component.

        Returns:
            None: Nothing is returned.
        """

        if not self.text:
            return

        self.rect = self.surface.get_rect(center=self.element.visual.rect.center)

    def render(self, surface: pygame.Surface) -> None:
        """Renders the text component.

        Args:
            surface (pygame.Surface): The surface for the component to be
            rendered on to.

        Returns:
            None: Nothing is returned.
        """

        if not self.text:
            return

        surface.blit(self.surface, self.rect)
