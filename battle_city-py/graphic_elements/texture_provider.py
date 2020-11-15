import os
import sys

import pygame


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


class TextureProvider:

    texture_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Textures")
    # texture_file = radius"F:\MyProgProject\BattleCity\Textures\\"
    textures = dict()

    @staticmethod
    def load_from_file(file_name):
        TextureProvider.textures[file_name] = pygame.image.load(os.path.join(TextureProvider.texture_file, file_name))
        # TextureProvider.textures[file_name] = pygame.image.load(resource_path(file_name))

    @staticmethod
    def load():
        TextureProvider.load_from_file("Bullet.png")
        TextureProvider.load_from_file("Tanks.png")
        TextureProvider.load_from_file("Ground.png")

    @staticmethod
    def resize(factor, name):
        TextureProvider.textures[name] = pygame.transform.scale(
            TextureProvider.textures[name],
            (
                int(TextureProvider.textures[name].get_rect().width * factor),
                int(TextureProvider.textures[name].get_rect().height * factor)
            )
        )

