import pygame

from pygame.constants import SYSTEM_CURSOR_ARROW, SYSTEM_CURSOR_HAND

from src.utilities.utility import Utility
from src.ui.button import Button
from src.ui.slider import Slider
from src.ui.container import Container


class UI:
    def __init__(self, app, path):
        self.app = app
        self.data = Utility.get_json_data(path)
        self.elements = []

        self.initialize()

    def initialize(self):
        for elements in self.data.keys():
            self.create_elements(elements)

    def create_elements(self, elements):
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

    def create_buttons(self):
        for button in self.data["buttons"]:
            self.elements.append(Button(self.app, **button))

    def create_containers(self):
        for container in self.data["containers"]:
            self.elements.append(Container(self.app, **container))

    def create_sliders(self):
        for slider in self.data["sliders"]:
            self.elements.append(Slider(self.app, **slider))

    def handle_hover(self):
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

    def update(self, event):
        self.handle_hover()

        for element in reversed(self.elements):
            element.update(event)

    def render(self, surface):
        for element in self.elements:
            element.render(surface)
