import os
from typing import Tuple

import pygame


class TextureImageInfo:
    def __init__(self, file_name: str, directory: str):
        self.file_name = file_name
        self.images = dict()
        self.textures = dict()
        print(os.path.join(
                directory,
                file_name,
            ))
        self.images[(1, 1)] = pygame.image.load(
            os.path.join(
                directory,
                file_name,
            )
        ).convert_alpha()
        self.textures["main"] = [
            self.images[(1, 1)].get_rect().x,
            self.images[(1, 1)].get_rect().y,
            self.images[(1, 1)].get_rect().w,
            self.images[(1, 1)].get_rect().h,
        ]

        self.add_size((2, 2))

    def add_texture(self, name: str, texture_rectangle: list):
        self.textures[name] = texture_rectangle

    def get_texture(self, name: str = "main", size: Tuple = (1, 1)) -> Tuple:
        return (
            self.images[size],
            [
                self.textures[name][0] * size[0],
                self.textures[name][1] * size[1],
                self.textures[name][2] * size[0],
                self.textures[name][3] * size[1],
            ],
        )

    def add_size(self, factor: Tuple):
        self.images[factor] = pygame.transform.scale(
            self.images[(1, 1)],
            (
                int(self.images[(1, 1)].get_rect().width * factor[0]),
                int(self.images[(1, 1)].get_rect().height * factor[1]),
            ),
        ).convert_alpha()
