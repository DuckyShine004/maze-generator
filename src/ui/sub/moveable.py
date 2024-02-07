import pygame


class Moveable:
    def __init__(self, element, **kwargs):
        self.element = element

        self.start = kwargs["start"]
        self.target = kwargs["target"]
        self.speed = kwargs["speed"]
        self.children = kwargs.get("children", [])

        self.is_moving = False
        self.is_moving_to_target = False

    def move_children(self):
        for child in self.children:
            self.move_elements_with_relation_to_child(child)

    def move_elements_with_relation_to_child(self, id):
        for element in self.element.app.ui.elements:
            if element.id != id:
                continue

            element.on_move()

    def on_move(self):
        self.is_moving = True
        self.is_moving_to_target ^= True
        self.move_children()

    def on_slide(self):
        if not self.is_moving:
            return

        if self.is_moving_to_target:
            self.slide_to_position(self.target)
        else:
            self.slide_to_position(self.start)

        self.element.text.on_slide()

    def stop_at_position(self, position):
        self.element.visual.image = pygame.transform.rotate(self.element.visual.image, 180)
        self.element.visual.rect.x = position[0]
        self.is_moving = False

    def slide_left_to_position(self, position):
        self.element.visual.rect.x -= self.speed

        if self.element.visual.rect.x <= position[0]:
            self.stop_at_position(position)

    def slide_right_to_position(self, position):
        self.element.visual.rect.x += self.speed

        if self.element.visual.rect.x >= position[0]:
            self.stop_at_position(position)

    def slide_to_position(self, position):
        if self.element.visual.rect.x > position[0]:
            self.slide_left_to_position(position)
            return

        self.slide_right_to_position(position)
