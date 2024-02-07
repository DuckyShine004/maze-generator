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
        while self.is_running:
            self.surface.fill(SURFACE_COLOR)
            self.__handle_events()

            current_time = pygame.time.get_ticks()

            if self.generator and (
                self.previous_time is None
                or (current_time - self.previous_time >= self.delay)
            ):
                try:
                    next(self.generator)
                    self.previous_time = current_time
                except StopIteration:
                    self.generator = None
                    self.previous_time = None

            self.update()
            self.render()

            pygame.display.flip()
            pygame.time.Clock().tick(60)

    def update(self):
        self.ui.update(self.event)

    def render(self):
        self.graph.render(self.surface)
        self.ui.render(self.surface)

    def __handle_events(self):
        for event in pygame.event.get():
            self.event = event

            if event.type == pygame.QUIT:
                self.is_running = False

            self.__handle_keyboard_events(event)
            self.__handle_mouse_events(event)

    def __handle_keyboard_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_running = False

    def __handle_mouse_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.graph.reset()
            self.generator = self.graph.generate()
