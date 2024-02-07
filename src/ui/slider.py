from src.ui.element import Element


class Slider(Element):
    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)

    def update(self, event):
        self.handle_slide()
