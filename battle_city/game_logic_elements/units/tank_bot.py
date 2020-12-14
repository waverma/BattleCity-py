import random

from battle_city.enums import Direction, UnitType
from battle_city.game_logic_elements.game_constants import (
    DEFAULT_TANK_HEALTH_POINTS,
    DEFAULT_TANK_SIZE,
    DEFAULT_TANK_SPEED,
)
from battle_city.game_logic_elements.units.tank import Tank
from battle_city.rect import Rect


class TankBot(Tank):
    def __init__(self):
        super().__init__()
        self.type = UnitType.TankWhite
        self.collision = Rect(w=DEFAULT_TANK_SIZE[0], h=DEFAULT_TANK_SIZE[1])
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

        current_x = x_saved + self.velocity[0]
        current_y = y_saved + self.velocity[1]

        field.try_remove_unit(self)
        while not field.try_place_unit(self, current_x, current_y):
            if current_x > x_saved:
                current_x -= 1
            if current_x < x_saved:
                current_x += 1
            if current_y > y_saved:
                current_y -= 1
            if current_y < y_saved:
                current_y += 1

        if x_saved == self.collision.x and y_saved == self.collision.y:
            self.set_velocity(self.directions[random.randint(0, 3)])
