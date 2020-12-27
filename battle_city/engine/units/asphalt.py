from battle_city.enums import UnitType, UpdateMode
from battle_city.engine.game_constants import (
    ASPHALT_HEALTH_POINTS,
    BIG_WALL_LENGTH,
    LITTLE_WALL_LENGTH,
)
from battle_city.engine.units.breakable_wall import BreakableWall
from battle_city.engine.units.unit import Unit
from battle_city.rect import Rect


class Asphalt(BreakableWall):
    def __init__(self, width=BIG_WALL_LENGTH, height=BIG_WALL_LENGTH):
        super().__init__(width, height)
        self.type = UnitType.Asphalt
        self.health_points = ASPHALT_HEALTH_POINTS
        self.update_mode = UpdateMode.NoneUpdate

        self.render_info = self.get_render_info_for_save()

    def on_explosion(self, field, explosion_rect: Rect):
        pass

    def is_intersected_with_unit(self, other: Unit) -> bool:
        return False

    def is_intersected_with_rect(self, rect: Unit) -> bool:
        return False

    def get_render_info(self):
        return self.get_render_info_for_save()

    def get_render_info_for_save(self):
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
