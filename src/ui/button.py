import pygame
from src.ui.element import Element


class Button(Element):
    def __init__(self, ui, **kwargs):
        super().__init__(ui, **kwargs)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.on_click(event)

        self.handle_slide()

    def on_click(self, event):
        if self.is_moving or not self.rect.collidepoint(event.pos):
            return

        match self.type:
            case "slide":
                self.on_move()
            case _:
                pass
