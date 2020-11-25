from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.game_constants import BUSH_HEALTH_POINTS, \
    BIG_WALL_LENGTH
from battle_city.game_logic_elements.units.breakable_wall import BreakableWall
from battle_city.game_logic_elements.units.unit import Unit
from battle_city.rect import Rect


class Bush(BreakableWall):
    def __init__(self, width=BIG_WALL_LENGTH, height=BIG_WALL_LENGTH):
        super().__init__(width, height)
        self.type = UnitType.Bush
        self.health_points = BUSH_HEALTH_POINTS

    def on_explosion(self, field, explosion_rect: Rect):
        pass

    def is_intersected_with_unit(self, other: Unit) -> bool:
        return False

    def is_intersected_with_rect(self, rect: Unit) -> bool:
        return False
