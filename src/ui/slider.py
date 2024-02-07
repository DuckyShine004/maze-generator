import pygame

from src.ui.element import Element
from src.utilities.utility import Utility


class Slider(Element):
    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

        self.width = kwargs["width"]
        self.radius = self.rect.w // 2

        self.min = self.target_position[0]
        self.max = self.min + kwargs["length"]

        self.is_dragging = False

    def on_click(self, event):
        if self.is_moving:
            return

        if not self.rect.collidepoint(event.pos):
            return

        self.is_dragging = True

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.on_click(event)

        self.on_drag(event)
        self.on_slide()

    def on_drag(self, event):
        if not self.is_dragging:
            return

        if not pygame.mouse.get_pressed()[0]:
            self.is_dragging = False
            return

        if event.type != pygame.MOUSEMOTION:
            return

        self.move_slider(event)

    def move_slider(self, event):
        position = event.pos[0] - self.radius

        self.rect.x = Utility.clamp(position, self.min, self.max)
        self.start_position[0] = self.rect.x + self.width
        self.target_position[0] = self.rect.x
