import os
from typing import Tuple

from battle_city.rect import Rect


class GraphicUtils:
    texture_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "Textures"
    )

    DEFAULT_CLIENT_SIZE = (32 * 26 + 150, 32 * 26)
    DEFAULT_GAME_FIELD_ELEMENT_SIZE = (32 * 26, 32 * 26)
    DEFAULT_WINDOW_SIZE = (32 * 26 + 150, 32 * 26)
    DEFAULT_MENU_COLLISION = Rect(0, 0,
                                  DEFAULT_WINDOW_SIZE[0],
                                  DEFAULT_WINDOW_SIZE[1])
    DEFAULT_GAME_FIELD_ELEMENT_COLLISION = Rect(
        0, 0,
        DEFAULT_GAME_FIELD_ELEMENT_SIZE[0],
        DEFAULT_GAME_FIELD_ELEMENT_SIZE[1]
    )

    WHITE_COLOR = (255, 255, 255)
    RED_GREEN_COLOR = (255, 255, 0)
    RED_BLUE_COLOR = (255, 0, 255)
    RED_COLOR = (255, 0, 0)
    GREEN_BLUE_COLOR = (0, 255, 255)
    GREEN_COLOR = (0, 255, 0)
    BLUE_COLOR = (0, 0, 255)
    BLACK_COLOR = (0, 0, 0)
    DEFAULT_DISPLAY_COLOR = (30, 213, 200)

    PARSE_SEPARATOR = "#=#=#=#=@@@@"

    TANKS = "Tanks.png"
    GROUND = "Ground.png"
    BULLET = "Bullet.png"

    BRICK_WALL = (GROUND, "BRICK_WALL")
    IRON_WALL = (GROUND, "IRON_WALL")
    WATER_GROUND_1 = (GROUND, "WATER_GROUND_1")
    WATER_GROUND_2 = (GROUND, "WATER_GROUND_2")
    GRASS_GROUND = (GROUND, "GRASS_GROUND")
    SEND_GROUND = (GROUND, "SEND_GROUND")
    ASS_FAULT = (GROUND, "ASS_FAULT")

    TANK_RED = (TANKS, "TANK_RED")
    TANK_WHITE = (TANKS, "TANK_WHITE")
    TANK_GREEN_ONE = (TANKS, "TANK_GREEN_ONE")
    TANK_BROWN = (TANKS, "TANK_BROWN")
    TANK_GREEN_TWO = (TANKS, "TANK_GREEN_TWO")
    TANK_ORANGE = (TANKS, "TANK_ORANGE")
    TANK_GREEN_THREE = (TANKS, "TANK_GREEN_THREE")

    BULLET_MAIN = (BULLET, "main")

    SPAWNER_1 = (TANKS, "SPAWNER_1")
    SPAWNER_2 = (TANKS, "SPAWNER_2")

    TANK_PRIORITY = 2
    BULLET_PRIORITY = 2
    SPAWNER_PRIORITY = 1
    WALLS_PRIORITY = 4
    ASS_FAULT_PRIORITY = 0
    SEND_PRIORITY = 0
    GRASS_PRIORITY = 3
    WATER_PRIORITY = 0

    @staticmethod
    def get_extended_texture_name(texture_name: Tuple, extend: str) -> Tuple:
        return (
            texture_name[0],
            texture_name[1] + GraphicUtils.PARSE_SEPARATOR + extend,
        )
