from src.utilities.utility import Utility


class Button:
    def __init__(self, position, images):
        self.images = Utility.get_images(images)
        self.current_image = self.images["default"]
        self.rect = self.current_image.get_rect(topleft=position)

    def update(self):
        pass

    def render(self, surface):
        surface.blit(self.current_image, self.rect)
