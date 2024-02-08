"""This module defines the lifecycle of the application."""

from typing import Optional

import pygame

from src.ui.ui import UI
from src.models.graph.graph import Graph

from src.constants.constants import SURFACE_COLOR, FPS, WIDTH, HEIGHT, MENU


class App:
    """The module for keeping the application running, or the module which defines
    the lifecycle of the application.

    Attributes:
        surface (pygame.Surface): The display surface.
        graph (Graph): Singleton instance of graph.
        ui (UI): Singleton instance of ui.
        event (pygame.Event): The current event.
        is_running (bool): Is the application running.
    """

    def __init__(self) -> None:
        """Initializes the application fields."""

        self.surface: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))

        self.graph: Graph = Graph()
        self.ui: UI = UI(self, MENU)

        self.event: Optional[pygame.Event] = None
        self.is_running: bool = True

    def run(self) -> None:
        """The main application loop."""

        clock = pygame.time.Clock()

        while self.is_running:
            self.surface.fill(SURFACE_COLOR)
            self.handle_events()

            self.update()
            self.render()

            pygame.display.flip()
            clock.tick(FPS)

    def update(self) -> None:
        """Updates the application."""

        self.graph.update()
        self.ui.update(self.event)

    def render(self) -> None:
        """Render application components."""

        self.graph.render(self.surface)
        self.ui.render(self.surface)

    def handle_events(self) -> None:
        """Handle peripheral events."""

        for event in pygame.event.get():
            self.event = event

            if event.type == pygame.QUIT:
                self.is_running = False

            self.handle_keyboard_events(event)

    def handle_keyboard_events(self, event: pygame.Event) -> None:
        """Handle keyboard events.

        Args:
            event (pygame.Event): The current event.
        """

        if event.type == pygame.KEYDOWN:
            self.handle_key_press(event.key)

    def handle_key_press(self, key: int) -> None:
        """Handle keyboard inputs.

        Args:
            key (int): The key code.
        """

        match key:
            case pygame.K_ESCAPE:
                self.is_running = False
            case _:
                pass
