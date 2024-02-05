import pygame

from src.constants.constants import WIDTH, HEIGHT


class App:
    def __init__(self):
        self.is_running = True
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        while self.is_running:
            self.handle_events()

            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            self.handle_keyboard_events(event)

    def handle_keyboard_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.is_running = False
