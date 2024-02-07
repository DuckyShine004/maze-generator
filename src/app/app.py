import pygame

from src.models.graph.graph import Graph
from src.constants.constants import SURFACE_COLOR, WIDTH, HEIGHT, MENU
from src.ui.ui import UI


class App:
    def __init__(self):
        self.is_running = True
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

        self.graph = Graph()
        self.ui = UI(self, MENU)

        self.generator = None
        self.previous_time = None
        self.delay = 10
        self.event = None

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
            if event.key == pygame.K_ESCAPE:
                self.is_running = False
