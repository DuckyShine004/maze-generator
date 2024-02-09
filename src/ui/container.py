"""This module allows for the creation of a container object."""

from typing import TYPE_CHECKING, Optional

import pygame

from src.ui.element import Element

if TYPE_CHECKING:
    from src.app.app import App


class Container(Element):
    """This class initializes the container component. The container
    component can contain a myriad of child components. It inherits
    from Element.
    """

    def __init__(self, app: "App", **kwargs) -> None:
        """Initializes the container component.

        Args:
            app (App): Singleton instance of app.
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        super().__init__(app, **kwargs)

    def update(self, _event: Optional[pygame.event.Event]) -> None:
        """Updates the container component.

        Args:
            _event (Optional[pygame.Event]): The current pygame event.
        """

        self.on_slide()
