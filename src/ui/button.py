"""This module allows for the creation of a button object."""

from typing import TYPE_CHECKING, Optional

import pygame

from src.ui.element import Element

if TYPE_CHECKING:
    from src.app.app import App


class Button(Element):
    """This class initializes the button component. The button
    component controls certain UI components, or even application
    functionalities."""

    def __init__(self, app: "App", **kwargs) -> None:
        """Initializes the button object.

        Args:
            app (App): Singleton instance of app.
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        super().__init__(app, **kwargs)

    def update(self, event: Optional[pygame.Event]) -> None:
        """Updates the button component.

        Args:
            event (Optional[pygame.Event]): The current pygame event.
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.on_click(event)

        self.on_slide()

    def on_click(self, event: Optional[pygame.Event]) -> None:
        """Handles the clicking of the button component.

        Args:
            event (Optional[pygame.Event]): The current pygame event.

        Returns:
            None: Nothing is returned.
        """

        if self.moveable.is_moving:
            return

        if not self.visual.rect.collidepoint(event.pos):
            return

        self.on_click_type()

    def on_click_type(self) -> None:
        """Handles the clicking of the button. This method handles
        selection buttons."""

        match self.type:
            case "default":
                pass
            case "slide":
                self.on_move()
            case "reset":
                self.app.graph.reset()
            case "generate":
                self.app.graph.generate()
            case _:
                self.app.graph.set_algorithm(self.type)
