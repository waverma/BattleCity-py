from graphic_elements.texture_provider import TextureProvider
from window import Window


if __name__ == "__main__":
    TextureProvider.set_textures()
    Window(32*26, 32*26).run()
