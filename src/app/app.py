import pygame

from src.ui.ui import UI
from src.models.graph.graph import Graph
from src.constants.constants import SURFACE_COLOR, WIDTH, HEIGHT, MENU


class App:
    def __init__(self):
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

        self.graph = Graph()
        self.ui = UI(self, MENU)

        self.event = None
        self.is_running = True

    def run(self):
        clock = pygame.time.Clock()

        while self.is_running:
            self.surface.fill(SURFACE_COLOR)
            self.handle_events()

            self.update()
            self.render()

            pygame.display.flip()
            clock.tick(60)

    def update(self):
        self.graph.update()
        self.ui.update(self.event)

    def render(self):
        self.graph.render(self.surface)
        self.ui.render(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            self.event = event

            if event.type == pygame.QUIT:
                self.is_running = False

            self.handle_keyboard_events(event)

    def handle_keyboard_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.handle_key_press(event.key)

    def handle_key_press(self, key):
        match key:
            case pygame.K_ESCAPE:
                self.is_running = False
            case _:
                pass
