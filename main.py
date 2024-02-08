"""The main driver code."""

import os
import pygame

from src.app.app import App

pygame.init()


def main() -> None:
    """Gets called if this is the module containing the main driver code."""

    os.environ["SDL_VIDEO_CENTERED"] = "1"

    app = App()
    app.run()


if __name__ == "__main__":
    main()
