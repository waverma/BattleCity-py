from unittest import TestCase
from enums.direction import Direction
from game_logic_elements.game_field import GameField
from pygame import Rect

from game_logic_elements.units.tank_bot import TankBot


class TestTankBot(TestCase):
    def test_move_step(self):
        field = GameField()
        tank = TankBot()
        tank.max_speed = 2
        tank.set_velocity(Direction.Up)

        self.assertTrue(field.try_place_unit(tank, 0, 0))

        tank.move_step(field)

        self.assertEqual(tank.collision,
                         Rect(0, 0, tank.collision.w, tank.collision.h))

        tank.set_velocity(Direction.Down)
        tank.move_step(field)

        self.assertNotEqual(tank.collision,
                            Rect(0, 0, tank.collision.w, tank.collision.h))
