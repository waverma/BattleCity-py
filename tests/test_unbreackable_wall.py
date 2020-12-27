from unittest import TestCase

from battle_city.enums import Direction, UnitType
from battle_city.engine.game_constants import LITTLE_WALL_LENGTH
from battle_city.engine.units.unbreakable_wall import (
    UnbreakableWall,
)
from battle_city.rect import Rect


class TestUnbreakableWall(TestCase):
    def test_get_render_info(self):
        wall = UnbreakableWall()
        wall.collision = Rect(
            0, 0, LITTLE_WALL_LENGTH * 5, LITTLE_WALL_LENGTH * 7
        )
        info = wall.get_render_info()

        self.assertEqual(len(info), 5 * 7)
        self.assertEqual(info[0][0], UnitType.IronWall)
        self.assertEqual(info[0][1].w, LITTLE_WALL_LENGTH)
        self.assertEqual(info[0][1].h, LITTLE_WALL_LENGTH)
        self.assertEqual(info[0][2], Direction.Up)
