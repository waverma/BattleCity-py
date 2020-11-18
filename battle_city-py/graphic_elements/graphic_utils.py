import os
from typing import Tuple

from pygame.rect import Rect


class GraphicUtils:
    texture_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Textures")

    parse_separator = "#=#=#=#=@@@@"

    tanks = "Tanks.png"
    ground = "Ground.png"
    bullet = "Bullet.png"

    BrickWall = (ground, "BrickWall")
    IronWall = (ground, "IronWall")
    GlassWall_1 = (ground, "GlassWall_1")
    GlassWall_2 = (ground, "GlassWall_2")
    GrassWall = (ground, "GrassWall")
    UnknownWall = (ground, "UnknownWall")

    TankRed = (tanks, "TankRed")
    TankWhite = (tanks, "TankWhite")
    TankGreenOne = (tanks, "TankGreenOne")
    TankBrown = (tanks, "TankBrown")
    TankGreenTwo = (tanks, "TankGreenTwo")
    TankOrange = (tanks, "TankOrange")
    TankGreenThree = (tanks, "TankGreenThree")

    Bullet = (bullet, "main")

    Spawner_1 = (tanks, "Spawner_1")
    Spawner_2 = (tanks, "Spawner_2")

    @staticmethod
    def get_extended_texture_name(texture_name: Tuple, extend: str) -> Tuple:
        return texture_name[0], texture_name[1] + GraphicUtils.parse_separator + extend
