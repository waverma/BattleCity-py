import os
import sys
from typing import Tuple

from battle_city.enums import TankTextureKind
from battle_city.view.graphic_utils import GraphicUtils
from battle_city.view.texture_image_info import TextureImageInfo


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


class TextureProvider:
    textures = dict()
    texture_file: str

    @staticmethod
    def set_textures(directory: str):
        TextureProvider.texture_file = os.path.join(
            directory, "resources", "textures"
        )
        TextureProvider.add_texture(GraphicUtils.GROUND)
        TextureProvider.textures[GraphicUtils.GROUND].add_texture(
            GraphicUtils.BRICK_WALL[1], [0, 0, 16, 16]
        )

        TextureProvider.textures[GraphicUtils.GROUND].add_texture(
            GraphicUtils.IRON_WALL[1], [0, 16, 16, 16]
        )

        TextureProvider.textures[GraphicUtils.GROUND].add_texture(
            GraphicUtils.WATER_GROUND_1[1], [0, 32, 16, 16]
        )

        TextureProvider.textures[GraphicUtils.GROUND].add_texture(
            GraphicUtils.WATER_GROUND_2[1], [0, 48, 16, 16]
        )

        TextureProvider.textures[GraphicUtils.GROUND].add_texture(
            GraphicUtils.GRASS_GROUND[1], [16, 32, 16, 16]
        )

        TextureProvider.textures[GraphicUtils.GROUND].add_texture(
            GraphicUtils.SEND_GROUND[1],
            [32, 32, 16, 16]
            # GraphicUtils.SEND_GROUND[1], [16, 48, 16, 16]
        )

        TextureProvider.textures[GraphicUtils.GROUND].add_texture(
            GraphicUtils.ASS_FAULT[1], [32, 48, 16, 16]
        )

        TextureProvider.textures[GraphicUtils.GROUND].add_size((2, 2))

        TextureProvider.add_texture(GraphicUtils.TANKS)
        TextureProvider.add_tank_kind(
            GraphicUtils.TANK_RED, TankTextureKind.Red, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TANK_WHITE, TankTextureKind.White, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TANK_GREEN_ONE, TankTextureKind.GreenOne, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TANK_BROWN, TankTextureKind.Brown, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TANK_GREEN_TWO, TankTextureKind.GreenTwo, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TANK_ORANGE, TankTextureKind.Orange, 0
        )

        TextureProvider.add_tank_kind(
            GraphicUtils.TANK_GREEN_THREE, TankTextureKind.GreenThree, 0
        )

        TextureProvider.textures[GraphicUtils.TANKS].add_texture(
            GraphicUtils.SPAWNER_1[1], [484, 288, 32, 32]
        )

        TextureProvider.textures[GraphicUtils.TANKS].add_texture(
            GraphicUtils.SPAWNER_2[1], [484 + 32, 288, 32, 32]
        )

        bonus_names = [
            GraphicUtils.BONUS_1[1],
            GraphicUtils.BONUS_2[1],
            GraphicUtils.BONUS_3[1],
            GraphicUtils.BONUS_4[1],
            GraphicUtils.BONUS_5[1],
            GraphicUtils.BONUS_6[1],
            GraphicUtils.BONUS_7[1],
            GraphicUtils.BONUS_8[1],
        ]

        for i in range(8):
            TextureProvider.textures[GraphicUtils.TANKS].add_texture(
                bonus_names[i], [960, 33 + i * 32, 32, 32]
            )

        TextureProvider.add_texture(GraphicUtils.BULLET)

    @staticmethod
    def add_texture(name: str):
        TextureProvider.textures[name] = TextureImageInfo(
            name, TextureProvider.texture_file
        )

    @staticmethod
    def add_tank_kind(
        texture_name: Tuple, tank_color: TankTextureKind, animation_step: int
    ):
        for direction in range(4):
            TextureProvider.textures[texture_name[0]].add_texture(
                texture_name[1]
                + GraphicUtils.PARSE_SEPARATOR
                + str(direction),
                TextureProvider.get_tank_image_rect(
                    tank_color, animation_step
                )[direction],
            )

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
