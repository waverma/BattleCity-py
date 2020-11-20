from unittest import TestCase

from enums.direction import Direction
from enums.unit_type import UnitType
from game_logic_elements.game_field import GameField
from game_logic_elements.units.breakable_wall import BreakableWall
from pygame import Rect


class TestBreakableWall(TestCase):
    def test_get_render_info(self):
        wall = BreakableWall()
        wall.collision = Rect(
            0, 0, wall.default_block_size * 5, wall.default_block_size * 7
        )
        info = wall.get_render_info()

        self.assertEqual(len(info), 5 * 7)
        self.assertEqual(info[0][0], UnitType.BrickWall)
        self.assertEqual(info[0][1].w, wall.default_block_size)
        self.assertEqual(info[0][1].h, wall.default_block_size)
        self.assertEqual(info[0][2], Direction.Up)

    def test_on_explosion(self):
        self.field = GameField()
        wall = BreakableWall()
        wall.collision = Rect(
            0, 0, wall.default_block_size * 5, wall.default_block_size * 7
        )
        self.field_rectangle = Rect(0, 0, self.field.width, self.field.height)
        self.field.try_place_unit(wall, 0, 0)
        wall.on_explosion(self.field, Rect(0, 0, 20, 20))

        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)),
            5 * 7 - 4,
        )
