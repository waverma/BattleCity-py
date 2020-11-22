from enums.unit_type import UnitType
from game_logic_elements.units.unit import Unit
from rect import Rect


class BreakableWall(Unit):
    default_block_size = 16

    def __init__(self, width=32, height=32):
        super().__init__()
        self.type = UnitType.BrickWall
        self.health_points = 0
        self.collision = Rect(-1, -1, width, height)

    def get_render_info(self):
        result = list()

        for x in range(
            self.collision.width // self.default_block_size
        ):
            for y in range(
                self.collision.height // self.default_block_size
            ):
                result.append((
                        self.type,
                        Rect(
                            self.collision.x + self.default_block_size * x,
                            self.collision.y + self.default_block_size * y,
                            self.default_block_size,
                            self.default_block_size,
                        ),
                        self.current_direction
                ))

        return result

    def on_explosion(self, field, explosion_rect: Rect):
        if self.health_points == 0:
            field.try_remove_unit(self)
            for x in range(self.collision.width // self.default_block_size):
                for y in range(
                    self.collision.height // self.default_block_size
                ):
                    if not explosion_rect.colliderect(
                        Rect(self.collision.x + x * self.default_block_size,
                             self.collision.y + y * self.default_block_size,
                             self.default_block_size,
                             self.default_block_size)
                    ):
                        field.try_place_unit(
                            BreakableWall(
                                self.default_block_size,
                                self.default_block_size,
                            ),
                            self.collision.x + x * self.default_block_size,
                            self.collision.y + y * self.default_block_size
                        )
        else:
            self.health_points -= 1
