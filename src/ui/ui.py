"""This module initializes, updates, and renders UI components."""

from typing import TYPE_CHECKING, List, Dict, Any, Optional

import pygame

from pygame.constants import SYSTEM_CURSOR_ARROW, SYSTEM_CURSOR_HAND

from src.ui.button import Button
from src.ui.slider import Slider
from src.ui.container import Container

from src.utilities.utility import Utility

if TYPE_CHECKING:
    from src.app.app import App


class UI:
    """This class initializes the user interface depending on which JSON
    configuration file is used.

    Attributes:
        app (App): Singleton instance of app.
        data (dict): JSON data for the current UI.
        elements (list): List of elements for the current UI.
    """

    def __init__(self, app: "App", path: str):
        """Initializes the user interface.

        Args:
            app (App): Singleton instance of app.
            path (str): The path to JSON defining the UI.
        """

        self.app: "App" = app
        self.data: Dict[str, Any] = Utility.get_json_data(path)
        self.elements: List[Any] = []

        self.initialize()

    def initialize(self) -> None:
        """Initializes the user interface components."""

        for elements in self.data.keys():
            self.create_elements(elements)

    def create_elements(self, elements: str) -> None:
        """Create user interface elements.

        Args:
            elements (str): The type of element to be created.
        """

        match elements:
            case "buttons":
                self.create_buttons()
            case "containers":
                self.create_containers()
            case "sliders":
                self.create_sliders()
            case _:
                pass

        self.elements.sort(key=lambda x: x.z_buffer, reverse=True)

    def create_buttons(self) -> None:
        """Create button components."""

        for button in self.data["buttons"]:
            self.elements.append(Button(self.app, **button))

    def create_containers(self) -> None:
        """Create container components."""

        for container in self.data["containers"]:
            self.elements.append(Container(self.app, **container))

    def create_sliders(self) -> None:
        """Create slider components."""

        for slider in self.data["sliders"]:
            self.elements.append(Slider(self.app, **slider))

    def handle_hover(self) -> None:
        """Handles the hovering of mouse over an element.

        Returns:
            None: Nothing is returned.
        """

        is_cursor_on_element = False

        for element in reversed(self.elements):
            if not isinstance(element, Button):
                break

            if element.is_hovered():
                is_cursor_on_element = True

        if is_cursor_on_element:
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            return

        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)

    def update(self, event: Optional[pygame.Event]) -> None:
        """Updates the user interface.

        Args:
            event (Optional[pygame.Event]): The current pygame event.
        """

        self.handle_hover()

        for element in reversed(self.elements):
            element.update(event)

    def render(self, surface: pygame.Surface) -> None:
        """Renders all user interface components.

        Args:
            surface (pygame.Surface): The surface for elements to be rendered on to.
        """

        for element in self.elements:
            element.render(surface)
