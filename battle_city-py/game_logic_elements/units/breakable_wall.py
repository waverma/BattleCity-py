from pygame.rect import Rect

from graphic_elements.draw_information import DrawInformation
from game_logic_elements.units.unit import Unit


class BreakableWall(Unit):
    default_block_size = 20
    texture_name = "Ground.png"
    texture_rect = [0, 0, 16 * 2, 16 * 2]  # TODO Перенести подобное в сонстанты графического пакета

    def __init__(self, width=40, height=40):
        super().__init__()
        self.health_points = 0
        self.collision = Rect(-1, -1, width, height)
        self.color = (255, 0, 0)

    def get_draw_info(self):
        result = list()

        for x in range(self.collision.width // BreakableWall.default_block_size):
            for y in range(self.collision.height // BreakableWall.default_block_size):
                result.append(DrawInformation(
                    texture_name=self.texture_name,
                    texture_rect=self.texture_rect,
                    draw_rect=Rect(
                        self.collision.x + BreakableWall.default_block_size * x,
                        self.collision.y + BreakableWall.default_block_size * y,
                        BreakableWall.default_block_size,
                        BreakableWall.default_block_size
                    )
                ))

        return result

    def on_explosion(self, field, explosion_rect: Rect):
        if self.health_points == 0:
            field.try_remove_unit(self)
            for x in range(self.collision.width // self.default_block_size):
                for y in range(self.collision.height // self.default_block_size):
                    if not explosion_rect.colliderect(
                            self.collision.x + x * self.default_block_size,
                            self.collision.y + y * self.default_block_size,
                            self.default_block_size,
                            self.default_block_size
                    ):
                        field.try_place_unit(
                            BreakableWall(
                                self.default_block_size,
                                self.default_block_size
                            ),
                            self.collision.x + x * self.default_block_size,
                            self.collision.y + y * self.default_block_size)
        else:
            self.health_points -= 1
