from src.utilities.utility import Utility
from src.ui.button import Button


class UI:
    def __init__(self, path):
        self.data = Utility.get_json_data(path)
        self.elements = []
        self.buttons = []

        self.initialize()

    def initialize(self):
        for button in self.data["buttons"]:
            self.buttons.append(Button(button["position"], button["images"]))

        self.elements.append(self.buttons)

    def render(self, surface):
        for element in self.elements:
            for sub_element in element:
                sub_element.render(surface)
