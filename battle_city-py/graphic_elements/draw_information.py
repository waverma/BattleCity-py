from pygame.rect import Rect


class DrawInformation:
    def __init__(
            self,
            transform=(0, 0, 1, 1),
            texture_name=None,
            draw_rect=Rect(0, 0, 0, 0),
            texture_rect=None,
            texture_rotate=None,
            fill_color=None,
            outline_color=None,
            outline_size=None,
            text=None,
            text_color=(0, 0, 0),
            text_size=36
    ):
        self.transform = transform
        self.texture_name = texture_name
        self.draw_rect = draw_rect
        self.texture_rect = texture_rect
        self.texture_rotate = texture_rotate
        self.fill_color = fill_color
        self.outline_color = outline_color
        self.outline_size = outline_size
        self.text = text
        self.text_size = text_size
        self.text_color = text_color

    def get_to_unpack(self) -> tuple:
        return (
            self.transform,
            self.texture_name,
            self.draw_rect,
            self.texture_rect,
            self.texture_rotate,
            self.fill_color,
            self.outline_color,
            self.outline_size,
            self.text,
            self.text_color,
            self.text_size
        )
