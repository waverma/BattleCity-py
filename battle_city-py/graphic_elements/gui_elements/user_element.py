from typing import Tuple

from buffers.buffer_to_game_logic import BufferToGameLogic
from buffers.buffer_to_render import BufferToRender
from buffers.user_event import UserEvent
from graphic_elements.draw_information import DrawInformation
from pygame.rect import Rect


class UserElement:
    def __init__(self, rect: Rect, absolute_position: Tuple):
        self.collision = rect
        self.absolute_position = absolute_position
        self.draw_info = DrawInformation(draw_rect=rect)

    def update(self, e: UserEvent, output_buffer: BufferToGameLogic):
        pass

    def get_render_info(
        self, transform: Tuple, buffer_to_render: BufferToRender
    ) -> list:
        pass
