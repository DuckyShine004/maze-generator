from src.utilities.utility import Utility


class Visual:
    def __init__(self, **kwargs):
        self.images = Utility.get_images(kwargs["images"])
        self.image = self.images["default"]

        self.rect = self.image.get_rect(topleft=kwargs["start"])

    def render(self, surface):
        surface.blit(self.image, self.rect)
