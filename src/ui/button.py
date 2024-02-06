import pygame
from pygame.constants import SYSTEM_CURSOR_ARROW, SYSTEM_CURSOR_HAND
from src.ui.element import Element


class Button(Element):
    def __init__(self, ui, **kwargs):
        super().__init__(ui, **kwargs)

    def update(self, event):
        self.on_hover()

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

    def on_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)
            return

        pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)
