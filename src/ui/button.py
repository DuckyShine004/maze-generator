import pygame
from src.ui.element import Element


class Button(Element):
    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.on_click(event)

        self.on_slide()

    def on_click(self, event):
        if self.is_moving:
            return

        if not self.rect.collidepoint(event.pos):
            return

        self.on_click_type()

    def on_click_type(self):
        match self.type:
            case "default":
                pass
            case "slide":
                self.on_move()
            case "reset":
                self.app.graph.reset()
            case "generate":
                self.app.graph.generate()
            case _:
                self.app.graph.set_algorithm(self.type)
