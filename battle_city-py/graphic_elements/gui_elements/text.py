from typing import Tuple

from pygame.rect import Rect

from buffers.buffer_to_render import BufferToRender
from graphic_elements.draw_information import DrawInformation
from graphic_elements.gui_elements.user_element import UserElement


class Text(UserElement):
    def __init__(self, rect: Rect, absolute_position: Tuple):
        super().__init__(rect, absolute_position)
        self.draw_info = DrawInformation(fill_color=(0, 0, 0), outline_color=(0, 0, 0), text_color=(0, 0, 0))
        self.is_focused = False

    def set_text(self, text: str):
        self.draw_info.text = text

    def get_render_info(self, transform: Tuple, buffer_to_render: BufferToRender):
        result = list()

        self.draw_info.transform = transform
        result.append(self.draw_info)

        return result
