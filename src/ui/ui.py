from src.utilities.utility import Utility
from src.ui.button import Button


class UI:
    def __init__(self, path):
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
            case _:
                pass

    def create_buttons(self):
        buttons = []

        for button in self.data["buttons"]:
            buttons.append(Button(**button))

        self.elements.append(buttons)

    def render(self, surface):
        for element in self.elements:
            for sub_element in element:
                sub_element.render(surface)
