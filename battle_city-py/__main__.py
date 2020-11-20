import os

from graphic_elements.texture_provider import TextureProvider
from window import Window

if __name__ == "__main__":
    TextureProvider.set_textures(
        os.path.normpath(
            os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir
        )
    )
    Window(32 * 26, 32 * 26).run()
