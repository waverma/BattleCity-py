from unittest import TestCase

from battle_city.enums import Direction
from battle_city.engine.game_field import GameField
from battle_city.engine.units.tank import Tank


class TestTank(TestCase):
    def test_shot(self):
        field = GameField()
        tank = Tank()
        field.try_place_unit(tank, 60, 60)

        tank.current_direction = Direction.Left
        tank.shot(field)
        self.assertEqual(len(field.units), 2)

        tank.current_direction = Direction.Down
        tank.shot(field)
        self.assertEqual(len(field.units), 2)

        tank.current_direction = Direction.Down
        tank.shot_await_tick_pointer = 0
        tank.shot(field)
        self.assertEqual(len(field.units), 3)

        tank.current_direction = Direction.Right
        tank.shot_await_tick_pointer = 0
        tank.shot(field)
        self.assertEqual(len(field.units), 4)

        tank.current_direction = Direction.Up
        tank.shot_await_tick_pointer = 0
        tank.shot(field)
        self.assertEqual(len(field.units), 5)

        tank.current_direction = Direction.Down
        tank.shot_await_tick_pointer = 0
        tank.shot(field)
        self.assertEqual(len(field.units), 6)
