from typing import Tuple

from buffers.buffer_to_game_logic import BufferToGameLogic
from buffers.buffer_to_render import BufferToRender
from buffers.user_event import UserEvent
from graphic_elements.draw_information import DrawInformation
from graphic_elements.gui_elements.button import Button
from graphic_elements.gui_elements.text import Text
from graphic_elements.gui_elements.user_element import UserElement
from pygame import Rect


class PostGameElement(UserElement):
    def __init__(self, rect: Rect, absolute_position: Tuple):
        super().__init__(rect, absolute_position)
        self.buttons = list()
        self.back_color = (255, 255, 255)
        self.text = Text(
            Rect(100, 300, 200, 25),
            (absolute_position[0], absolute_position[1]),
        )

        self.restart_button = Button(
            Rect(100, 100, 600, 100),
            (absolute_position[0], absolute_position[1]),
        )
        self.restart_button.draw_info.fill_color = (255, 255, 0)
        self.restart_button.focused_outline_color = (255, 0, 0)
        self.restart_button.draw_info.outline_size = 3
        self.restart_button.draw_info.text = "Перезапустить"

        self.exit_button = Button(
            Rect(100, 600, 600, 100),
            (absolute_position[0], absolute_position[1]),
        )
        self.exit_button.draw_info.fill_color = (255, 255, 0)
        self.exit_button.focused_outline_color = (255, 0, 0)
        self.exit_button.draw_info.outline_size = 3
        self.exit_button.draw_info.text = "В главное меню"

        self.buttons.append(self.restart_button)
        self.buttons.append(self.exit_button)
        self.text_size = 36
        self.text_color = (255, 0, 255)

    def update(self, e: UserEvent, output_buffer: BufferToGameLogic):
        for button in self.buttons:
            button.update(e, output_buffer)

        output_buffer.restart_request = self.restart_button.is_clicked
        output_buffer.is_to_main_menu_button_pressed = (
            self.exit_button.is_clicked
        )

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

        self.text.draw_info.text = "{}! Очки: {}".format(
            buffer_to_render.battle_result,
            buffer_to_render.points
        )
        text_render_info = self.text.get_render_info(
            new_transform, buffer_to_render
        )
        for text_render_info_parts in text_render_info:
            result.append(text_render_info_parts)

        return result
