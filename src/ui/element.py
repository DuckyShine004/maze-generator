import pygame

from src.utilities.utility import Utility
from src.constants.constants import FONT_COLOR, FONT_SIZE


class Element:
    def __init__(self, app, **kwargs):
        self.app = app
        self.id = kwargs["id"]
        self.start_position = kwargs["position"]
        self.target_position = kwargs["target_position"]
        self.related_elements = kwargs.get("related_elements", [])
        self.images = Utility.get_images(kwargs["images"])
        self.current_image = self.images["default"]
        self.rect = self.current_image.get_rect(topleft=kwargs["position"])
        self.text = kwargs.get("text", "")
        font_path = kwargs.get("font_path", None)
        font_size = kwargs.get("font_size", FONT_SIZE)
        font_color = kwargs.get("font_color", FONT_COLOR)
        self.font = pygame.font.Font(font_path, font_size)
        self.text_surface = self.font.render(self.text, True, font_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.type = kwargs["type"]
        self.speed = kwargs["speed"]
        self.z_buffer = kwargs["z-buffer"]
        self.is_moving = False
        self.is_moving_to_target_position = False

    def move_related_elements(self):
        for element_id in self.related_elements:
            for element in self.app.ui.elements:
                if element.id == element_id:
                    element.on_move()

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def on_move(self):
        self.is_moving = True
        self.is_moving_to_target_position ^= True
        self.move_related_elements()

    def handle_slide(self):
        if not self.is_moving:
            return

        if self.is_moving_to_target_position:
            if self.rect.x > self.target_position[0]:
                self.rect.x -= self.speed

                if self.rect.x <= self.target_position[0]:
                    self.rect.x = self.target_position[0]
                    self.is_moving = False
                    self.current_image = self.images.get("flipped", self.current_image)
        else:
            if self.rect.x < self.start_position[0]:
                self.rect.x += self.speed

                if self.rect.x >= self.start_position[0]:
                    self.rect.x = self.start_position[0]
                    self.is_moving = False
                    self.current_image = self.images["default"]

        if not self.text:
            return

        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def render(self, surface):
        surface.blit(self.current_image, self.rect)

        if not self.text:
            return

        surface.blit(self.text_surface, self.text_rect)
