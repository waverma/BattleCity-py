from typing import Tuple

from battle_city.buffers.buffer_to_game_logic import BufferToGameLogic
from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.buffers.user_event import UserEvent
from battle_city.view.draw_information import DrawInformation
from battle_city.rect import Rect


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
