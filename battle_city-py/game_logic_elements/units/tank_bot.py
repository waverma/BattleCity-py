import random

from enums.direction import Direction
from game_logic_elements.units.tank import Tank


class TankBot(Tank):
    def __init__(self):
        super().__init__()

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
