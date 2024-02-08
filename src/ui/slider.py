"""This module allows for the creation of a slider object."""

from typing import TYPE_CHECKING, Optional

import pygame

from src.ui.element import Element

from src.utilities.utility import Utility

from src.constants.constants import GRAPH_DELAY

if TYPE_CHECKING:
    from src.app.app import App


class Slider(Element):
    """This class initializes the slider component. The slider
    component controls certain UI components.

    Attributes:
        is_dragging (bool): Description
        length (float): Description
        max (float): Description
        min (float): Description
        radius (float): Description
        width (float): Description
    """

    def __init__(self, app: "App", **kwargs) -> None:
        """Initializes the slider object.

        Args:
            app (App): Singleton instance of app.
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        super().__init__(app, **kwargs)

        self.width: float = kwargs["width"]
        self.length: float = kwargs["length"]
        self.radius: float = self.visual.rect.w / 2

        self.min: float = self.moveable.target[0]
        self.max: float = self.min + kwargs["length"]

        self.is_dragging: bool = False

    def move_slider(self, event: Optional[pygame.Event]) -> None:
        """Moves the slider's position relative to the cursor's position.

        Args:
            event (Optional[pygame.Event]): The current pygame event.
        """

        position = event.pos[0] - self.radius

        self.visual.rect.x = Utility.clamp(position, self.min, self.max)
        self.moveable.start[0] = self.visual.rect.x + self.width
        self.moveable.target[0] = self.visual.rect.x

        self.update_delay()

    def on_click(self, event: Optional[pygame.Event]) -> None:
        """Handles the clicking of the slider component.

        Args:
            event (Optional[pygame.Event]): The current pygame event.

        Returns:
            None: Nothing is being returned.
        """

        if self.moveable.is_moving:
            return

        if not self.visual.rect.collidepoint(event.pos):
            return

        self.is_dragging = True

    def on_drag(self, event: Optional[pygame.Event]) -> None:
        """Handles the dragging of the slider component.

        Args:
            event (Optional[pygame.Event]): The current pygame event.

        Returns:
            None: Nothing is being returned.
        """

        if not self.is_dragging:
            return

        if not pygame.mouse.get_pressed()[0]:
            self.is_dragging = False
            return

        if event.type != pygame.MOUSEMOTION:
            return

        self.move_slider(event)

    def update_delay(self) -> None:
        """Updates the graph animation speed."""

        percentage = (self.visual.rect.x - self.min) / self.length
        self.app.graph.delay = percentage * GRAPH_DELAY

    def update(self, event: Optional[pygame.Event]) -> None:
        """Updates the slider component.

        Args:
            event (Optional[pygame.Event]): The current pygame event.
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.on_click(event)

        self.on_drag(event)
        self.on_slide()
