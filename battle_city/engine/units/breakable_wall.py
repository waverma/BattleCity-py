from battle_city.enums import UnitType, UpdateMode
from battle_city.engine.game_constants import (
    BIG_WALL_LENGTH,
    BRICK_HEALTH_POINTS,
    LITTLE_WALL_LENGTH,
)
from battle_city.engine.units.unit import Unit
from battle_city.rect import Rect


class BreakableWall(Unit):
    def __init__(self, width=BIG_WALL_LENGTH, height=BIG_WALL_LENGTH):
        super().__init__()
        self.type = UnitType.BrickWall
        self.health_points = BRICK_HEALTH_POINTS
        self.collision = Rect(w=width, h=height)
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

    def on_explosion(self, field, explosion_rect: Rect):
        self.health_points -= 1
        if self.health_points <= 0:
            field.try_remove_unit(self)
            for x in range(self.collision.width // LITTLE_WALL_LENGTH):
                for y in range(self.collision.height // LITTLE_WALL_LENGTH):
                    if not explosion_rect.colliderect(
                        Rect(
                            self.collision.x + x * LITTLE_WALL_LENGTH,
                            self.collision.y + y * LITTLE_WALL_LENGTH,
                            LITTLE_WALL_LENGTH,
                            LITTLE_WALL_LENGTH,
                        )
                    ):
                        field.try_place_unit(
                            BreakableWall(
                                LITTLE_WALL_LENGTH,
                                LITTLE_WALL_LENGTH,
                            ),
                            self.collision.x + x * LITTLE_WALL_LENGTH,
                            self.collision.y + y * LITTLE_WALL_LENGTH,
                        )
