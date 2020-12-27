import os

from battle_city.game_loop import GameLoop
from battle_city.view.graphic_utils import GraphicUtils
from battle_city.view.texture_provider import TextureProvider


if __name__ == "__main__":

    game_loop = GameLoop(
        GraphicUtils.DEFAULT_CLIENT_SIZE[0],
        GraphicUtils.DEFAULT_CLIENT_SIZE[1],
    )

    TextureProvider.set_textures(
        os.path.normpath(
            os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir
        )
    )

    #
    # Для собирания в ехе
    # print(os.path.normpath(
    #         os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir
    #     ))
    # TextureProvider.set_textures(
    #     os.path.normpath(
    #         os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir + os.sep + os.pardir + os.sep + os.pardir
    #     )
    # )

    game_loop.run()
