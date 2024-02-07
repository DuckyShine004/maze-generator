import pygame

from src.ui.element import Element
from src.utilities.utility import Utility


class Slider(Element):
    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)
        self.is_dragging = False
        self.offset = 20
        self.slide_width = kwargs["slide_width"]
        self.min = self.target_position[0]
        self.max = self.min + kwargs["length"]

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.is_moving and self.rect.collidepoint(event.pos):
                self.is_dragging = True

        if self.is_dragging:
            if pygame.mouse.get_pressed()[0]:
                if event.type == pygame.MOUSEMOTION:
                    self.rect.x = Utility.clamp(
                        event.pos[0] - self.offset,
                        self.min,
                        self.max,
                    )

                    self.target_position[0] = self.rect.x
                    self.start_position[0] = self.rect.x + self.slide_width
            else:
                self.is_dragging = False

        self.handle_slide()

    def on_drag(self, event):
        if self.is_moving or not self.rect.collidepoint(event.pos):
            return

        self.is_dragging = True
