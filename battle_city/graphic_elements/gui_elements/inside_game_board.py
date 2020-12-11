from typing import Tuple

from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.enums import Direction
from battle_city.graphic_elements.draw_information import DrawInformation
from battle_city.graphic_elements.gui_elements.user_element import UserElement
from battle_city.rect import Rect


def get_draw_info(transform: Tuple, text: str, shift: int) -> DrawInformation:
    return DrawInformation(
        transform=(transform[0] + 10,
                   transform[1] + shift,
                   transform[2],
                   transform[3]),
        text_size=20,
        text=text,
        text_color=(255, 255, 255)
    )


class InsideGameBoard(UserElement):
    def __init__(self, rect: Rect, absolute_position: Tuple):
        super().__init__(rect, absolute_position)

        self.kills = ""
        self.hp = ""
        self.speed = ""
        self.cool_dawn = ""
        self.bonus_cool_dawn = ""

    def get_render_info(
        self, transform: Tuple, buffer_to_render: BufferToRender
    ) -> list:
        result = list()

        self.hp = "HP: " + str(buffer_to_render.health_points)
        self.kills = "Kills: " + str(buffer_to_render.points[0])
        self.speed = "Speed: " + str(buffer_to_render.speed)
        self.cool_dawn = "CD: {} | {}".format(buffer_to_render.cool_dawn[0],
                                              buffer_to_render.cool_dawn[1])

        if buffer_to_render.bonus_cool_dawn[2] is not None:
            self.bonus_cool_dawn = "{} | {}".format(
                buffer_to_render.bonus_cool_dawn[0],
                buffer_to_render.bonus_cool_dawn[1]
            )

            result.append(
                DrawInformation.get_info_by(
                    buffer_to_render.bonus_cool_dawn[2],
                    Rect(transform[0] + 10, transform[1] + 100, transform[2], transform[3]),
                    Direction.Null
                )
            )
            result.append(get_draw_info(transform, self.bonus_cool_dawn, 160))

        result.append(get_draw_info(transform, self.hp, 10))
        result.append(get_draw_info(transform, self.kills, 30))
        result.append(get_draw_info(transform, self.speed, 50))
        result.append(get_draw_info(transform, self.cool_dawn, 70))

        return result
