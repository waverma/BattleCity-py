import os
import sys
from typing import Tuple

from battle_city.enums.tank_texture_kind import TankTextureKind
from battle_city.graphic_elements.graphic_utils import GraphicUtils
from battle_city.graphic_elements.texture_image_info import TextureImageInfo


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


class TextureProvider:
    textures = dict()
    texture_file: str

    tanks = "Tanks.png"
    ground = "Ground.png"
    bullet = "Bullet.png"

    @staticmethod
    def set_textures(directory: str):
        TextureProvider.texture_file = os.path.join(directory, "textures")
        TextureProvider.add_texture(TextureProvider.ground)
        TextureProvider.textures[TextureProvider.ground].add_texture(
            GraphicUtils.BrickWall[1], [0, 0, 16, 16]
        )

        TextureProvider.textures[TextureProvider.ground].add_texture(
            GraphicUtils.IronWall[1], [0, 16, 16, 16]
        )

        TextureProvider.textures[TextureProvider.ground].add_texture(
            GraphicUtils.GlassWall_1[1], [0, 32, 16, 16]
        )

        TextureProvider.textures[TextureProvider.ground].add_texture(
            GraphicUtils.GlassWall_2[1], [0, 48, 16, 16]
        )

        TextureProvider.textures[TextureProvider.ground].add_texture(
            GraphicUtils.GrassWall[1], [16, 32, 16, 16]
        )

        TextureProvider.textures[TextureProvider.ground].add_texture(
            GraphicUtils.UnknownWall[1], [32, 32, 16, 16]
        )

        TextureProvider.textures[TextureProvider.ground].add_size((2, 2))

        TextureProvider.add_texture(TextureProvider.tanks)
        TextureProvider.add_tank_kind(
            GraphicUtils.TankRed, TankTextureKind.Red, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TankWhite, TankTextureKind.White, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TankGreenOne, TankTextureKind.GreenOne, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TankBrown, TankTextureKind.Brown, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TankGreenTwo, TankTextureKind.GreenTwo, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TankOrange, TankTextureKind.Orange, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TankGreenThree, TankTextureKind.GreenThree, 0
        )

        TextureProvider.textures[TextureProvider.tanks].add_texture(
            GraphicUtils.Spawner_1[1], [484, 288, 32, 32]
        )

        TextureProvider.textures[TextureProvider.tanks].add_texture(
            GraphicUtils.Spawner_2[1], [484 + 32, 288, 32, 32]
        )

        TextureProvider.add_texture(TextureProvider.bullet)

    @staticmethod
    def add_texture(name: str):
        TextureProvider.textures[name] = TextureImageInfo(
            name,
            TextureProvider.texture_file
        )

    @staticmethod
    def add_tank_kind(
        texture_name: Tuple, tank_color: TankTextureKind, animation_step: int
    ):
        for direction in range(4):
            TextureProvider.textures[texture_name[0]].add_texture(
                texture_name[1]
                + GraphicUtils.parse_separator
                + str(direction),
                TextureProvider.get_tank_image_rect(
                    tank_color, animation_step
                )[direction],
            )

    @staticmethod
    def get_tank_image_rect(
            tank_color: TankTextureKind,
            animation_step: int
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
