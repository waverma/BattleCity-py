from typing import Tuple

from battle_city.buffers.buffer_to_game_logic import BufferToGameLogic
from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.buffers.user_event import UserEvent
from battle_city.view.draw_information import DrawInformation
from battle_city.view.graphic_utils import GraphicUtils
from battle_city.view.gui_elements.button import Button
from battle_city.view.gui_elements.user_element import UserElement
from battle_city.rect import Rect


class SinglePlayMenu(UserElement):
    def __init__(self, rect: Rect, absolute_position: Tuple):
        super().__init__(rect, absolute_position)
        self.buttons = list()
        self.back_color = GraphicUtils.WHITE_COLOR

        self.new_game_button = Button(
            Rect(100, 100, 750, 100),
            (absolute_position[0], absolute_position[1]),
            "Новая игра",
        )

        self.exit_button = Button(
            Rect(100, 300, 750, 100),
            (absolute_position[0], absolute_position[1]),
            "Назад",
        )

        self.buttons.append(self.new_game_button)
        self.buttons.append(self.exit_button)

    def update(self, e: UserEvent, output_buffer: BufferToGameLogic):
        for button in self.buttons:
            button.update(e, output_buffer)
        output_buffer.is_new_game_button_pressed = (
            self.new_game_button.is_clicked
        )
        output_buffer.is_cancel_button_pressed = self.exit_button.is_clicked

    def get_render_info(
        self, transform: Tuple, buffer_to_render: BufferToRender
    ):
        new_transform = (
            transform[0] + self.collision.x,
            transform[1] + self.collision.y,
            1,
            1,
        )
        result = list()
        result.append(
            DrawInformation(
                transform=transform,
                draw_rect=self.collision,
                fill_color=self.back_color,
            )
        )

        for button in self.buttons:
            button_info = button.get_render_info(
                new_transform, buffer_to_render
            )
            for button_info_parts in button_info:
                result.append(button_info_parts)

        return result
