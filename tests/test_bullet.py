from unittest import TestCase
from battle_city.enums import Direction
from battle_city.game_logic_elements.game_constants import LITTLE_WALL_LENGTH
from battle_city.game_logic_elements.game_field import GameField
from battle_city.game_logic_elements.units.breakable_wall import BreakableWall
from battle_city.game_logic_elements.units.bullet import Bullet
from battle_city.game_logic_elements.units.tank import Tank
from battle_city.rect import Rect


class TestBullet(TestCase):
    def test_move_step(self):
        self.field = GameField()
        wall = BreakableWall()
        wall.collision = Rect(
            0, 0, LITTLE_WALL_LENGTH * 5, LITTLE_WALL_LENGTH * 7
        )
        self.field_rectangle = Rect(0, 0, self.field.width, self.field.height)
        self.field.try_place_unit(wall, 0, 0)
        bullet = Bullet(Tank())
        bullet.current_direction = Direction.Left
        self.field.try_place_unit(bullet, LITTLE_WALL_LENGTH * 5 + 1, 1)

        bullet.move_step(self.field)

        self.assertEqual(
            len(self.field.get_intersected_units(self.field_rectangle)),
            5 * 7 - 2,
        )
