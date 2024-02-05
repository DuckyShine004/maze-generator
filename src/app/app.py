import pygame

from src.models.graph.graph import Graph
from src.constants.constants import SURFACE_COLOR, WIDTH, HEIGHT


class App:
    def __init__(self):
        self.is_running = True
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

        self.graph = Graph()
        self.graph.generate()

    def run(self):
        while self.is_running:
            self.surface.fill(SURFACE_COLOR)
            self.__handle_events()

            self.graph.render(self.surface)
            pygame.display.flip()

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            self.__handle_keyboard_events(event)

    def __handle_keyboard_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_running = False
