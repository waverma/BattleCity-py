from unittest import TestCase
from enums.direction import Direction
from game_logic_elements.units.unit import Unit
from rect import Rect


def get_unit():
    unit = Unit()
    unit.velocity = (0, 0)
    unit.current_direction = Direction.Null
    return unit


class TestUnit(TestCase):
    def test_set_velocity(self):
        unit = get_unit()
        unit.set_velocity(Direction.Up)
        self.assertEqual(unit.current_direction, Direction.Up)
        self.assertEqual(unit.velocity[0], 0)
        self.assertEqual(unit.velocity[1], -unit.max_speed)

        unit = get_unit()
        unit.set_velocity(Direction.Down)
        self.assertEqual(unit.current_direction, Direction.Down)
        self.assertEqual(unit.velocity[0], 0)
        self.assertEqual(unit.velocity[1], unit.max_speed)

        unit = get_unit()
        unit.set_velocity(Direction.Right)
        self.assertEqual(unit.current_direction, Direction.Right)
        self.assertEqual(unit.velocity[0], unit.max_speed)
        self.assertEqual(unit.velocity[1], 0)

        unit = get_unit()
        unit.set_velocity(Direction.Left)
        self.assertEqual(unit.current_direction, Direction.Left)
        self.assertEqual(unit.velocity[0], -unit.max_speed)
        self.assertEqual(unit.velocity[1], 0)

        unit.set_velocity(Direction.Null)
        self.assertEqual(unit.current_direction, Direction.Left)
        self.assertEqual(unit.velocity[0], 0)
        self.assertEqual(unit.velocity[1], 0)

    def test_is_intersected_with_rect(self):
        unit = get_unit()
        unit.collision = Rect(1, 1, 20, 20)
        rect1 = Rect(3, 3, 22, 22)
        rect2 = Rect(1, 1, 0, 0)
        rect3 = Rect(111, 111, 111, 111)
        rect4 = Rect(5, 5, 5, 5)
        rect5 = Rect(0, 0, 111, 111)

        self.assertTrue(unit.is_intersected_with_rect(rect1))
        self.assertTrue(unit.is_intersected_with_rect(rect2))
        self.assertFalse(unit.is_intersected_with_rect(rect3))
        self.assertTrue(unit.is_intersected_with_rect(rect4))
        self.assertTrue(unit.is_intersected_with_rect(rect5))
