from src.ui.element import Element


class Container(Element):
    def __init__(self, ui, **kwargs):
        super().__init__(ui, **kwargs)

    def update(self, event):
        self.handle_slide()
