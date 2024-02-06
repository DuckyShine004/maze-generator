from src.utilities.utility import Utility


class Element:
    def __init__(self, ui, **kwargs):
        self.ui = ui
        self.id = kwargs["id"]
        self.start_position = kwargs["position"]
        self.target_position = kwargs["target_position"]
        self.related_elements = kwargs["related_elements"]
        self.images = Utility.get_images(kwargs["images"])
        self.current_image = self.images["default"]
        self.rect = self.current_image.get_rect(topleft=kwargs["position"])
        self.type = kwargs["type"]
        self.speed = kwargs["speed"]
        self.is_moving = False
        self.is_moving_to_target_position = False

    def move_related_elements(self):
        for element_id in self.related_elements:
            for element in self.ui.elements:
                if element.id == element_id:
                    element.on_move()

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
                    self.current_image = self.images["flipped"]
        else:
            if self.rect.x < self.start_position[0]:
                self.rect.x += self.speed

                if self.rect.x >= self.start_position[0]:
                    self.rect.x = self.start_position[0]
                    self.is_moving = False
                    self.current_image = self.images["default"]

    def render(self, surface):
        surface.blit(self.current_image, self.rect)
