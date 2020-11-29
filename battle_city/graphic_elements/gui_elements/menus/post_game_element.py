from typing import Tuple

from battle_city.buffers.buffer_to_game_logic import BufferToGameLogic
from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.buffers.user_event import UserEvent
from battle_city.graphic_elements.draw_information import DrawInformation
from battle_city.graphic_elements.graphic_utils import GraphicUtils
from battle_city.graphic_elements.gui_elements.button import Button
from battle_city.graphic_elements.gui_elements.text import Text
from battle_city.graphic_elements.gui_elements.user_element import UserElement
from battle_city.rect import Rect


class PostGameElement(UserElement):
    def __init__(self, rect: Rect, absolute_position: Tuple):
        super().__init__(rect, absolute_position)
        self.buttons = list()
        self.back_color = GraphicUtils.WHITE_COLOR
        self.text = Text(
            Rect(100, 300, 200, 25),
            (absolute_position[0], absolute_position[1]),
        )

        self.restart_button = Button(
            Rect(100, 100, 750, 100),
            (absolute_position[0], absolute_position[1]),
            "Перезапустить"
        )

        self.exit_button = Button(
            Rect(100, 600, 750, 100),
            (absolute_position[0], absolute_position[1]),
            "В главное меню"
        )

        self.buttons.append(self.restart_button)
        self.buttons.append(self.exit_button)
        self.text_size = 10
        self.text_color = GraphicUtils.RED_BLUE_COLOR

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

        if buffer_to_render.battle_result[1]:
            end_battle_message = "Победа!"
        else:
            end_battle_message = "Поражение"

        kills = "Обычные: {}\n Броникованные: {}\n Восстанавливающиеся{}\n Скорострельные{}".format(
            buffer_to_render.points[1],
            buffer_to_render.points[2],
            buffer_to_render.points[3],
            buffer_to_render.points[4],
        )

        self.text.draw_info.text = "{} Очки: {}".format(
            end_battle_message,
            kills
        )
        self.text.draw_info.text_size = 15
        text_render_info = self.text.get_render_info(
            new_transform, buffer_to_render
        )
        for text_render_info_parts in text_render_info:
            result.append(text_render_info_parts)

        return result
