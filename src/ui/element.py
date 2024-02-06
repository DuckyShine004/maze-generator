from src.utilities.utility import Utility


class Element:
    def __init__(self, **kwargs):
        self.images = Utility.get_images(kwargs["images"])
        self.current_image = self.images["default"]
        self.rect = self.current_image.get_rect(topleft=kwargs["position"])

    def render(self, surface):
        surface.blit(self.current_image, self.rect)
