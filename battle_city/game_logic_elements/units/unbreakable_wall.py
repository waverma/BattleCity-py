from battle_city.enums import UnitType, UpdateMode
from battle_city.game_logic_elements.game_constants import (
    BIG_WALL_LENGTH,
    IRON_HEALTH_POINTS,
    LITTLE_WALL_LENGTH,
)
from battle_city.game_logic_elements.units.unit import Unit
from battle_city.rect import Rect


class UnbreakableWall(Unit):
    def __init__(self, width=BIG_WALL_LENGTH, height=BIG_WALL_LENGTH):
        super().__init__()
        self.collision = Rect(-1, -1, width, height)
        self.type = UnitType.IronWall
        self.health_points = IRON_HEALTH_POINTS

        self.update_mode = UpdateMode.IntersectOnly

    def get_render_info(self):
        result = list()

        for x in range(self.collision.width // LITTLE_WALL_LENGTH):
            for y in range(self.collision.height // LITTLE_WALL_LENGTH):
                result.append(
                    (
                        self.type,
                        Rect(
                            self.collision.x + LITTLE_WALL_LENGTH * x,
                            self.collision.y + LITTLE_WALL_LENGTH * y,
                            LITTLE_WALL_LENGTH,
                            LITTLE_WALL_LENGTH,
                        ),
                        self.current_direction,
                    )
                )

        return result
