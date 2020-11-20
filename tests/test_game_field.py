from unittest import TestCase
from game_logic_elements.game_field import GameField
from game_logic_elements.units.breakable_wall import BreakableWall
from game_logic_elements.units.bullet import Bullet
from game_logic_elements.units.tank import Tank
from game_logic_elements.units.unit import Unit
from pygame import Rect


def get_default_unit() -> Unit:
    unit = Unit()
    unit.collision = Rect(0, 0, 2, 2)
    return unit


class TestGameField(TestCase):
    def test_try_place_unit(self):
        self.field = GameField()
        self.field_rectangle = Rect(0, 0, self.field.width, self.field.height)

        self.assertTrue(self.field.try_place_unit(get_default_unit(), 1, 1))
        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)), 1
        )

        self.assertFalse(self.field.try_place_unit(get_default_unit(), 1, 1))
        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)), 1
        )

        self.assertTrue(self.field.try_place_unit(get_default_unit(), 4, 4))
        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)), 2
        )

        self.assertFalse(self.field.try_place_unit(get_default_unit(), -1, -1))
        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)), 2
        )

        self.assertFalse(
            self.field.try_place_unit(get_default_unit(), 2, 56465435)
        )
        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)), 2
        )

    def test_try_remove_unit(self):
        self.field = GameField()
        self.field_rectangle = Rect(0, 0, self.field.width, self.field.height)

        unit = get_default_unit()
        self.field.try_place_unit(unit, 1, 1)
        self.assertTrue(self.field.try_remove_unit(unit))
        self.field.update()
        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)), 0
        )

    def test_explode(self):
        self.field = GameField()
        self.field_rectangle = Rect(0, 0, self.field.width, self.field.height)
        self.field.try_place_unit(BreakableWall(16, 16), 1, 1)
        self.field.try_place_unit(BreakableWall(16, 16), 3, 1)
        self.field.try_place_unit(BreakableWall(16, 16), 6, 1)
        self.field.try_place_unit(BreakableWall(16, 16), 77, 1)
        self.field.try_place_unit(BreakableWall(16, 16), 300, 1)
        self.field.try_place_unit(BreakableWall(16, 16), 26, 1)

        self.field.explode(Bullet(Tank()), 200, Rect(0, 0, 6, 6))

        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)), 1
        )

        self.field = GameField()
        self.field.try_place_unit(BreakableWall(32, 32), 20, 20)
        self.field.explode(Bullet(Tank()), 10, Rect(20, 20, 6, 6))
        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)), 3
        )
