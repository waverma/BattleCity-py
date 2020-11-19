from unittest import TestCase

from enums.direction import Direction
from game_logic_elements.game_field import GameField
from game_logic_elements.units.breakable_wall import BreakableWall
from game_logic_elements.units.bullet import Bullet
from game_logic_elements.units.tank import Tank
from pygame import Rect


class TestBullet(TestCase):
    def test_move_step(self):
        self.field = GameField()
        wall = BreakableWall()
        wall.collision = Rect(
            0, 0, wall.default_block_size * 5, wall.default_block_size * 7
        )
        self.field_rectangle = Rect(0, 0, self.field.width, self.field.height)
        self.field.try_place_unit(wall, 0, 0)
        bullet = Bullet(Tank())
        bullet.current_direction = Direction.Left
        self.field.try_place_unit(bullet, wall.default_block_size * 5 + 1, 1)

        bullet.move_step(self.field)

        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)),
            5 * 7 - 2,
        )
