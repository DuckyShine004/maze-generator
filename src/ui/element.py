import pygame

from src.ui.sub.moveable import Moveable
from src.ui.sub.visual import Visual
from src.ui.sub.text import Text

from src.utilities.utility import Utility
from src.constants.constants import FONT_COLOR, FONT_SIZE


class Element(object):
    def __init__(self, app, **kwargs):
        self.app = app

        self.id = kwargs["id"]
        self.type = kwargs["type"]
        self.z_buffer = kwargs["z-buffer"]

        self.moveable = Moveable(self, **kwargs)
        self.visual = Visual(**kwargs)
        self.text = Text(self, **kwargs)

    def is_hovered(self):
        if self.type == "default":
            return False

        return self.visual.rect.collidepoint(pygame.mouse.get_pos())

    def on_move(self):
        self.moveable.on_move()

    def on_slide(self):
        self.moveable.on_slide()
        self.text.on_slide()

    def render(self, surface):
        self.visual.render(surface)
        self.text.render(surface)
