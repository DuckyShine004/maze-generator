import pygame

from src.constants.constants import FONT_COLOR, FONT_SIZE


class Text:
    def __init__(self, element, **kwargs):
        self.element = element

        self.text = kwargs.get("text", "")

        font_path = kwargs.get("font_path", None)
        font_size = kwargs.get("font_size", FONT_SIZE)
        font_color = kwargs.get("font_color", FONT_COLOR)

        self.font = pygame.font.Font(font_path, font_size)

        self.surface = self.font.render(self.text, True, font_color)
        self.rect = self.surface.get_rect(center=self.element.visual.rect.center)

    def on_slide(self):
        if not self.text:
            return

        self.rect = self.surface.get_rect(center=self.element.visual.rect.center)

    def render(self, surface):
        if not self.text:
            return

        surface.blit(self.surface, self.rect)
