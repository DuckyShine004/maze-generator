"""This module allows for the creation of moveable components."""

from typing import TYPE_CHECKING, List, Tuple

import pygame

if TYPE_CHECKING:
    from src.ui.element import Element


class Moveable:
    """This class initializes the moveable component. A moveable component
    is any component that requires moving.

    Attributes:
        children (list): Child components that require moving.
        element (Element): The element that requires text rendering.
        is_moving (bool): Is the current component moving.
        is_moving_to_target (bool): Is the current component moving to
        the target position.
        speed (float): The speed at which the component should move.
        start (tuple): The start position of the component.
        target (tuple): The target position of the component.
    """

    def __init__(self, element: "Element", **kwargs) -> None:
        """Initializes the moveable component object.

        Args:
            element (Element): Instance of user interface element.
            **kwargs: Keyworded, variable-length argument dictionary.
        """

        self.element: "Element" = element

        self.start: Tuple[float, float] = kwargs["start"]
        self.target: Tuple[float, float] = kwargs["target"]
        self.speed: float = kwargs["speed"]
        self.children: List[str] = kwargs.get("children", [])

        self.is_moving: bool = False
        self.is_moving_to_target: bool = False

    def move_children(self) -> None:
        """Move all child components."""

        for identifier in self.children:
            self.move_elements_with_relation_to_child(identifier)

    def move_elements_with_relation_to_child(self, identifier) -> None:
        """Move all elements that have identifiers equal to the input
        identifier.

        Args:
            identifier (str): The child component's identifier.
        """

        for element in self.element.app.ui.elements:
            if element.id != identifier:
                continue

            element.on_move()

    def on_move(self) -> None:
        """Handles the movement of the moveable component."""

        self.is_moving = True
        self.is_moving_to_target ^= True
        self.move_children()

    def on_slide(self) -> None:
        """Handles the sliding movement of the moveable component.

        Returns:
            None: Nothing is being returned.
        """

        if not self.is_moving:
            return

        if self.is_moving_to_target:
            self.slide_to_position(self.target)
        else:
            self.slide_to_position(self.start)

        self.element.text.on_slide()

    def stop_at_position(self, position: Tuple[float, float]) -> None:
        """Stop at the input position.

        Args:
            position (Tuple[float, float]): The position to move to.
        """

        self.element.visual.image = pygame.transform.rotate(self.element.visual.image, 180)
        self.element.visual.rect.x = position[0]
        self.is_moving = False

    def slide_left_to_position(self, position: Tuple[float, float]) -> None:
        """Move from the current hitbox position to the input position.
        Direction of movement is to the left.

        Args:
            position (Tuple[float, float]): The position to move to.
        """

        self.element.visual.rect.x -= self.speed

        if self.element.visual.rect.x <= position[0]:
            self.stop_at_position(position)

    def slide_right_to_position(self, position: Tuple[float, float]) -> None:
        """Move from the current hitbox position to the input position.
        Direction of movement is to the right.

        Args:
            position (Tuple[float, float]): The position to move to.
        """

        self.element.visual.rect.x += self.speed

        if self.element.visual.rect.x >= position[0]:
            self.stop_at_position(position)

    def slide_to_position(self, position: Tuple[float, float]) -> None:
        """Move from the current hitbox position to the input position.

        Args:
            position (Tuple[float, float]): The position to move to.

        Returns:
            None: Nothing is being returned.
        """

        if self.element.visual.rect.x > position[0]:
            self.slide_left_to_position(position)
            return

        self.slide_right_to_position(position)
