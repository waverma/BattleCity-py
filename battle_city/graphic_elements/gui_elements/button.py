from typing import Tuple

from battle_city.buffers.buffer_to_game_logic import BufferToGameLogic
from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.buffers.user_event import UserEvent
from battle_city.graphic_elements.gui_elements.user_element import UserElement
from battle_city.rect import Rect


class Button(UserElement):
    def __init__(self, rect: Rect, absolute_position: Tuple):
        super().__init__(rect, absolute_position)
        self.actions = list()
        self.draw_info.fill_color = (0, 0, 0)
        self.focused_outline_color = (0, 0, 0)
        self.draw_info.outline_size = 0

        self.is_focused = False
        self.is_clicked = False

    def add_action(self, action):
        self.actions.append(action)

    def update(self, e: UserEvent, output_buffer: BufferToGameLogic):
        self.is_clicked = False
        self.is_focused = Rect(
            self.collision.x + self.absolute_position[0],
            self.collision.y + self.absolute_position[1],
            self.collision.width,
            self.collision.height,
        ).collidepoint(
            e.absolute_mouse_location[0], e.absolute_mouse_location[1]
        )

        if self.is_focused:
            if e.is_left_mouse_click and not e.was_left_mouse_click:
                self.is_clicked = True
                for action in self.actions:
                    action()

    def get_render_info(
        self, transform: Tuple, buffer_to_render: BufferToRender
    ):
        result = list()

        self.draw_info.outline_color = None
        self.draw_info.transform = transform
        if self.is_focused:
            self.draw_info.outline_color = self.focused_outline_color
        result.append(self.draw_info)

        return result
