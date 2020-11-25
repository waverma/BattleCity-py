import random

from battle_city.enums.direction import Direction
from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.game_constants import \
    DEFAULT_TANK_HEALTH_POINTS, DEFAULT_TANK_SPEED, DEFAULT_TANK_SIZE
from battle_city.game_logic_elements.units.tank import Tank
from battle_city.rect import Rect


class TankBot(Tank):
    def __init__(self):
        super().__init__()
        self.type = UnitType.TankWhite
        self.collision = Rect(-1, -1, DEFAULT_TANK_SIZE[0],
                              DEFAULT_TANK_SIZE[1])
        self.max_speed = DEFAULT_TANK_SPEED
        self.health_points = DEFAULT_TANK_HEALTH_POINTS

        self.opposite_directions = {
            Direction.Down: Direction.Up,
            Direction.Up: Direction.Down,
            Direction.Right: Direction.Left,
            Direction.Left: Direction.Right,
        }

        self.directions = [
            Direction.Down,
            Direction.Up,
            Direction.Right,
            Direction.Left,
        ]

    def step(self, field):
        super().step(field)
        self.shot(field)

    def move_step(self, field):
        x_saved = self.collision.x
        y_saved = self.collision.y

        field.try_remove_unit(self)
        if not field.try_place_unit(
            self, x_saved + self.velocity[0], y_saved + self.velocity[1]
        ):
            field.try_place_unit(self, x_saved, y_saved)
            self.set_velocity(self.directions[random.randint(0, 3)])
