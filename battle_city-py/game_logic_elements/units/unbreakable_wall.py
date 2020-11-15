from pygame.rect import Rect

from graphic_elements.draw_information import DrawInformation
from game_logic_elements.units.unit import Unit


class UnbreakableWall(Unit):
    default_block_size = 20
    texture_name = "Ground.png"
    texture_rect = [0, 16 * 2, 16 * 2, 16 * 2]  # TODO Перенести в константы графики

    def __init__(self, width=40, height=40):
        super().__init__()
        self.collision = Rect(-1, -1, width, height)

    def get_draw_info(self) -> list:
        result = list()

        for x in range(self.collision.width // UnbreakableWall.default_block_size):
            for y in range(self.collision.height // UnbreakableWall.default_block_size):
                result.append(DrawInformation(
                    texture_name=self.texture_name,
                    draw_rect=Rect(
                        self.collision.x + UnbreakableWall.default_block_size * x,
                        self.collision.y + UnbreakableWall.default_block_size * y,
                        UnbreakableWall.default_block_size,
                        UnbreakableWall.default_block_size
                    ),
                    texture_rect=self.texture_rect
                ))

        return result
