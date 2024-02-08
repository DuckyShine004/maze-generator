"""Summary
"""
import pygame

from pygame.constants import SYSTEM_CURSOR_ARROW, SYSTEM_CURSOR_HAND

from src.ui.button import Button
from src.ui.slider import Slider
from src.ui.container import Container

from src.utilities.utility import Utility


class UI:
    """Summary

    Attributes:
        app (TYPE): Description
        data (TYPE): Description
        elements (list): Description
    """

    def __init__(self, app, path):
        """Summary

        Args:
            app (TYPE): Description
            path (TYPE): Description
        """

        self.app = app
        self.data = Utility.get_json_data(path)
        self.elements = []

        self.initialize()

    def initialize(self) -> None:
        """Summary"""

        for elements in self.data.keys():
            self.create_elements(elements)

    def create_elements(self, elements) -> None:
        """Summary

        Args:
            elements (TYPE): Description
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
        """Summary"""

        for button in self.data["buttons"]:
            self.elements.append(Button(self.app, **button))

    def create_containers(self) -> None:
        """Summary"""

        for container in self.data["containers"]:
            self.elements.append(Container(self.app, **container))

    def create_sliders(self) -> None:
        """Summary"""

        for slider in self.data["sliders"]:
            self.elements.append(Slider(self.app, **slider))

    def handle_hover(self) -> None:
        """Summary

        Returns:
            None: Nothing is returned
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

    def update(self, event) -> None:
        """Updates the user interface.

        Args:
            event (TYPE): Description
        """

        self.handle_hover()

        for element in reversed(self.elements):
            element.update(event)

    def render(self, surface) -> None:
        """Summary

        Args:
            surface (TYPE): Description
        """

        for element in self.elements:
            element.render(surface)
