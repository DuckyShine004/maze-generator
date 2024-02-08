import os
import pygame

from src.app.app import App

pygame.init()


def main():
    os.environ["SDL_VIDEO_CENTERED"] = "1"

    app = App()
    app.run()


if __name__ == "__main__":
    main()
