import os

from graphic_elements.texture_provider import TextureProvider
from game_loop import GameLoop

if __name__ == "__main__":
    TextureProvider.set_textures(
        os.path.normpath(
            os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir
        )
    )
    GameLoop(32 * 26, 32 * 26).run()
