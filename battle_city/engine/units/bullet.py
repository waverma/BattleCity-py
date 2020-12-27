from battle_city.enums import Direction, UnitType, UpdateMode
from battle_city.engine.game_constants import (
    DEFAULT_BULLET_SIZE,
    DEFAULT_BULLET_SPEED,
    DEFAULT_EXPLOSION_LENGTH,
)
from battle_city.engine.units.unit import Unit
from battle_city.rect import Rect


class Bullet(Unit):
    def __init__(self, owner: Unit):
        super().__init__()
        self.collision = Rect(
            w=DEFAULT_BULLET_SIZE[0], h=DEFAULT_BULLET_SIZE[1]
        )
        self.max_speed = DEFAULT_BULLET_SPEED
        self.current_direction = Direction.Up
        self.owner = owner
        self.explosion_radius = DEFAULT_EXPLOSION_LENGTH
        self.type = UnitType.Bullet
        self.update_mode = UpdateMode.StepOnly

    def move_step(self, field):
        x_saved = self.collision.x
        y_saved = self.collision.y
        self.set_velocity(self.current_direction)

        field.try_remove_unit(self)
        if not field.try_place_unit(
            self, x_saved + self.velocity[0], y_saved + self.velocity[1]
        ):
            units = field.get_intersected_units(
                Rect(
                    x_saved + self.velocity[0],
                    y_saved + self.velocity[1],
                    self.collision.width,
                    self.collision.height,
                )
            )
            field.explode(self, self.explosion_radius, self.collision, units)

    def on_explosion(self, field, explosion_rect: Rect):
        field.try_remove_unit(self)
