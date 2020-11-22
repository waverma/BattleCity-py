from unittest import TestCase
from enums.direction import Direction
from enums.unit_type import UnitType
from game_logic_elements.units.unbreakable_wall import UnbreakableWall
from rect import Rect


class TestUnbreakableWall(TestCase):
    def test_get_render_info(self):
        wall = UnbreakableWall()
        wall.collision = Rect(
            0, 0, wall.default_block_size * 5, wall.default_block_size * 7
        )
        info = wall.get_render_info()

        self.assertEqual(len(info), 5 * 7)
        self.assertEqual(info[0][0], UnitType.IronWall)
        self.assertEqual(info[0][1].w, wall.default_block_size)
        self.assertEqual(info[0][1].h, wall.default_block_size)
        self.assertEqual(info[0][2], Direction.Up)
