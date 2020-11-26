from typing import Tuple

import pygame
from battle_city.buffers.buffer_to_game_logic import BufferToGameLogic
from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.buffers.user_event import UserEvent
from battle_city.enums.direction import Direction
from battle_city.graphic_elements.draw_information import DrawInformation
from battle_city.graphic_elements.gui_elements.text import Text
from battle_city.graphic_elements.gui_elements.user_element import UserElement
from battle_city.rect import Rect


class GameFieldElement(UserElement):
    def __init__(self, rect, absolute_position):
        super().__init__(rect, absolute_position)
        self.text = Text(
            Rect(0, 0, 50, 25), (absolute_position[0], absolute_position[1])
        )
        self.text.draw_info.text_size = 17
        self.text.draw_info.text_color = (0, 255, 0)

    def update(self, e: UserEvent, output_buffer: BufferToGameLogic):
        output_buffer.user_prepare_direction = Direction.Null

        if len(e.pressed_buttons) > 0:
            if e.pressed_buttons[pygame.K_w]:
                output_buffer.user_prepare_direction = Direction.Up
            elif e.pressed_buttons[pygame.K_a]:
                output_buffer.user_prepare_direction = Direction.Left
            elif e.pressed_buttons[pygame.K_s]:
                output_buffer.user_prepare_direction = Direction.Down
            elif e.pressed_buttons[pygame.K_d]:
                output_buffer.user_prepare_direction = Direction.Right
            output_buffer.shot_request = e.pressed_buttons[pygame.K_SPACE]
            output_buffer.is_pause_request = (
                e.pressed_buttons[pygame.K_ESCAPE]
                and len(e.non_released_buttons) > 0
                and not e.non_released_buttons[pygame.K_ESCAPE]
                and not output_buffer.is_chat_open
            )

    def get_render_info(
        self, transform: Tuple, buffer_to_render: BufferToRender
    ) -> list:
        new_transform = (
            transform[0] + self.collision.x,
            transform[1] + self.collision.y,
            self.collision.width / buffer_to_render.field_size[0],
            self.collision.height / buffer_to_render.field_size[1],
        )

        result = list()
        result.append(
            DrawInformation(
                transform=transform,
                draw_rect=self.collision,
                fill_color=(0, 0, 0),
            )
        )

        priority_lists = dict()

        for unit_render_info in buffer_to_render.units:
            for unit_render_info_parts in unit_render_info:
                draw_info = DrawInformation.get_info_by(
                    *unit_render_info_parts
                )
                draw_info.transform = new_transform
                if draw_info.render_priority not in priority_lists:
                    priority_lists[draw_info.render_priority] = list()
                priority_lists[draw_info.render_priority].append(draw_info)

        for player_render_info_parts in buffer_to_render.player:
            draw_info = DrawInformation.get_info_by(*player_render_info_parts)
            draw_info.transform = new_transform
            if draw_info.render_priority not in priority_lists:
                priority_lists[draw_info.render_priority] = list()
            priority_lists[draw_info.render_priority].append(draw_info)

        for units_priority in sorted(priority_lists.keys()):
            for unit in priority_lists[units_priority]:
                result.append(unit)

        self.text.draw_info.text = "HP: {})==( Reload: {}".format(
            str(buffer_to_render.health_points),
            buffer_to_render.cool_dawn
        )
        self.text.draw_info.collision = Rect(
            buffer_to_render.player[0][1].x + 30,
            buffer_to_render.player[0][1].y - 10,
            20,
            12,
        )
        text_render_info = self.text.get_render_info(
            new_transform, buffer_to_render
        )

        for text_render_info_parts in text_render_info:
            result.append(text_render_info_parts)

        return result
