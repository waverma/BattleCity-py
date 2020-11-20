from unittest import TestCase
from enums.direction import Direction
from game_logic_elements.game_field import GameField
from game_logic_elements.units.tank import Tank
from pygame import Rect


class TestTank(TestCase):
    def test_shot(self):
        field = GameField()
        field_rectangle = Rect(0, 0, field.width, field.height)
        tank = Tank()
        field.try_place_unit(tank, 60, 60)

        tank.current_direction = Direction.Left
        tank.shot(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 2)

        tank.current_direction = Direction.Down
        tank.shot(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 2)

        tank.current_direction = Direction.Down
        tank.shot_await_tick_pointer = 0
        tank.shot(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 3)

        tank.current_direction = Direction.Right
        tank.shot_await_tick_pointer = 0
        tank.shot(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 4)

        tank.current_direction = Direction.Up
        tank.shot_await_tick_pointer = 0
        tank.shot(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 5)

        tank.current_direction = Direction.Down
        tank.shot_await_tick_pointer = 0
        tank.shot(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 5)
