from pygame.rect import Rect

from enums.unit_type import UnitType
from enums.direction import Direction
from game_logic_elements.units.unit import Unit


class Bullet(Unit):
    def __init__(self, owner: Unit):
        super().__init__()
        self.collision = Rect(-1, -1, 8, 8)
        self.max_speed = 6
        self.current_direction = Direction.Up
        self.owner = owner
        self.type = UnitType.Bullet

    def step(self, field: 'GameField'):
        super().step(field)

    def move_step(self, field: 'GameField'):
        x_saved = self.collision.left
        y_saved = self.collision.top

        field.try_remove_unit(self)
        if not field.try_place_unit(self, x_saved + self.velocity[0], y_saved + self.velocity[1]):
            units = field.get_intersected_units(Rect(
                x_saved + self.velocity[0],
                y_saved + self.velocity[1],
                self.collision.width,
                self.collision.height
            ))
            field.explode(self, 34, self.collision, units)

    def on_explosion(self, field: 'GameField', explosion_rect: Rect):
        field.try_remove_unit(self)
