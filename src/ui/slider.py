import pygame

from src.ui.element import Element

from src.utilities.utility import Utility

from src.constants.constants import GRAPH_DELAY


class Slider(Element):
    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

        self.width = kwargs["width"]
        self.length = kwargs["length"]
        self.radius = self.visual.rect.w // 2

        self.min = self.moveable.target[0]
        self.max = self.min + kwargs["length"]

        self.is_dragging = False

    def move_slider(self, event):
        position = event.pos[0] - self.radius

        self.visual.rect.x = Utility.clamp(position, self.min, self.max)
        self.moveable.start[0] = self.visual.rect.x + self.width
        self.moveable.target[0] = self.visual.rect.x

        self.update_delay()

    def on_click(self, event):
        if self.moveable.is_moving:
            return

        if not self.visual.rect.collidepoint(event.pos):
            return

        self.is_dragging = True

    def on_drag(self, event):
        if not self.is_dragging:
            return

        if not pygame.mouse.get_pressed()[0]:
            self.is_dragging = False
            return

        if event.type != pygame.MOUSEMOTION:
            return

        self.move_slider(event)

    def update_delay(self):
        percentage = (self.visual.rect.x - self.min) / self.length
        self.app.graph.delay = percentage * GRAPH_DELAY

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.on_click(event)

        self.on_drag(event)
        self.on_slide()
