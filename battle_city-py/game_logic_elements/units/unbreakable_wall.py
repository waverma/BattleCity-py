from enums.unit_type import UnitType
from game_logic_elements.units.unit import Unit
from rect import Rect


class UnbreakableWall(Unit):
    default_block_size = 16

    def __init__(self, width=32, height=32):
        super().__init__()
        self.collision = Rect(-1, -1, width, height)
        self.type = UnitType.IronWall

    def get_render_info(self):
        result = list()

        for x in range(self.collision.width // self.default_block_size):
            for y in range(self.collision.height // self.default_block_size):
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
