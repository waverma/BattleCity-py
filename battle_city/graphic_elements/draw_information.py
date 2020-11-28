from typing import Tuple

from battle_city.enums.direction import Direction
from battle_city.enums.tank_texture_kind import TankTextureKind
from battle_city.enums.unit_type import UnitType
from battle_city.graphic_elements.graphic_utils import GraphicUtils
from battle_city.rect import Rect


def puck_info(
    info: "DrawInformation",
    direction: Direction,
    name: Tuple,
    kind: TankTextureKind,
):
    info.texture_name = GraphicUtils.get_extended_texture_name(
        name, str(int(direction))
    )
    info.texture_rect = DrawInformation.get_tank_image_rect(kind, 0)[
        int(direction)
    ]


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
        text_size=36,
        image_transform=(1, 1),
        render_priority=0
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
        self.image_transform = image_transform
        self.render_priority = render_priority

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
            self.text_size,
            self.image_transform,
        )

    @staticmethod
    def get_info_by(
        unit_type: UnitType, collision: Rect, direction: Direction
    ) -> "DrawInformation":
        info = DrawInformation(draw_rect=collision, image_transform=(2, 2))

        if (
            unit_type == UnitType.TankBot
            or unit_type == UnitType.TankPlayer
            or unit_type == UnitType.TankRival
        ):
            puck_info(
                info, direction, GraphicUtils.TANK_RED, TankTextureKind.Red
            )

        elif unit_type == UnitType.BrickWall:
            info.texture_name = GraphicUtils.BRICK_WALL
            info.render_priority = GraphicUtils.WALLS_PRIORITY

        elif unit_type == UnitType.IronWall:
            info.texture_name = GraphicUtils.IRON_WALL
            info.render_priority = GraphicUtils.WALLS_PRIORITY

        elif unit_type == UnitType.Bush:
            info.texture_name = GraphicUtils.GRASS_GROUND
            info.render_priority = GraphicUtils.GRASS_PRIORITY

        elif unit_type == UnitType.Fire:
            info.texture_name = GraphicUtils.WATER_GROUND_2
            info.render_priority = GraphicUtils.ASS_FAULT_PRIORITY

        elif unit_type == UnitType.Dirt:
            info.texture_name = GraphicUtils.SEND_GROUND
            info.render_priority = GraphicUtils.SEND_PRIORITY

        elif unit_type == UnitType.Asphalt:
            info.texture_name = GraphicUtils.ASS_FAULT
            info.render_priority = GraphicUtils.ASS_FAULT_PRIORITY

        elif unit_type == UnitType.PlayerSpawner:
            info.texture_name = GraphicUtils.SPAWNER_1
            info.render_priority = GraphicUtils.SPAWNER_PRIORITY

        elif unit_type == UnitType.RivalSpawner:
            info.texture_name = GraphicUtils.SPAWNER_2
            info.render_priority = GraphicUtils.SPAWNER_PRIORITY

        elif unit_type == UnitType.BotSpawner:
            info.texture_name = GraphicUtils.SPAWNER_2
            info.render_priority = GraphicUtils.SPAWNER_PRIORITY

        elif unit_type == UnitType.Bullet:
            if direction == Direction.Up:
                info.texture_rotate = 90 * 3
            elif direction == Direction.Down:
                info.texture_rotate = 90
            elif direction == Direction.Right:
                info.texture_rotate = 90 * 2
            elif direction == Direction.Left:
                info.texture_rotate = 0
            info.texture_name = GraphicUtils.BULLET_MAIN
            info.render_priority = GraphicUtils.BULLET_PRIORITY

        elif unit_type == UnitType.TankRed:
            puck_info(
                info, direction, GraphicUtils.TANK_RED, TankTextureKind.Red
            )
            info.render_priority = GraphicUtils.TANK_PRIORITY

        elif unit_type == UnitType.TankWhite:
            puck_info(
                info, direction, GraphicUtils.TANK_WHITE, TankTextureKind.White
            )
            info.render_priority = GraphicUtils.TANK_PRIORITY

        elif unit_type == UnitType.TankGreenOne:
            puck_info(
                info,
                direction,
                GraphicUtils.TANK_GREEN_ONE,
                TankTextureKind.GreenOne,
            )
            info.render_priority = GraphicUtils.TANK_PRIORITY

        elif unit_type == UnitType.TankBrown:
            puck_info(
                info, direction, GraphicUtils.TANK_BROWN, TankTextureKind.Brown
            )
            info.render_priority = GraphicUtils.TANK_PRIORITY

        elif unit_type == UnitType.TankGreenTwo:
            puck_info(
                info,
                direction,
                GraphicUtils.TANK_GREEN_TWO,
                TankTextureKind.GreenTwo,
            )
            info.render_priority = GraphicUtils.TANK_PRIORITY

        elif unit_type == UnitType.TankOrange:
            puck_info(
                info,
                direction,
                GraphicUtils.TANK_ORANGE,
                TankTextureKind.Orange,
            )
            info.render_priority = GraphicUtils.TANK_PRIORITY

        elif unit_type == UnitType.TankGreenThree:
            puck_info(
                info,
                direction,
                GraphicUtils.TANK_GREEN_THREE,
                TankTextureKind.GreenThree,
            )
            info.render_priority = GraphicUtils.TANK_PRIORITY

        return info

    @staticmethod
    def get_tank_image_rect(
        tank_color: TankTextureKind, animation_step: int
    ) -> tuple:
        tank_block = (32 * 4, 32)
        tank = (32, 32)

        return (
            [
                tank_color * tank_block[0],
                tank_block[1] * animation_step,
                tank[0],
                tank[1],
            ],
            [
                tank_color * tank_block[0] + tank[0] * 1,
                tank_block[1] * animation_step,
                tank[0],
                tank[1],
            ],
            [
                tank_color * tank_block[0] + tank[0] * 2,
                tank_block[1] * animation_step,
                tank[0],
                tank[1],
            ],
            [
                tank_color * tank_block[0] + tank[0] * 3,
                tank_block[1] * animation_step,
                tank[0],
                tank[1],
            ],
        )
