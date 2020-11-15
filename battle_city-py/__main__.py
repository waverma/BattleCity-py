from graphic_elements.texture_provider import TextureProvider
from window import Window


if __name__ == "__main__":
    TextureProvider.load()
    TextureProvider.resize(1.9, "Tanks.png")
    TextureProvider.resize(2, "Ground.png")
    Window(1000, 1000).run()
