from enums.direction import Direction
from enums.unit_type import UnitType
from game_logic_elements.units.unit import Unit
from rect import Rect


class Bullet(Unit):
    def __init__(self, owner: Unit):
        super().__init__()
        self.collision = Rect(-1, -1, 8, 8)
        self.max_speed = 6
        self.current_direction = Direction.Up
        self.owner = owner
        self.explosion_radius = 34
        self.type = UnitType.Bullet

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
