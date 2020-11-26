from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.game_constants import BIG_WALL_LENGTH, \
    ASPHALT_HEALTH_POINTS
from battle_city.game_logic_elements.units.breakable_wall import BreakableWall
from battle_city.game_logic_elements.units.unit import Unit
from battle_city.rect import Rect


class Asphalt(BreakableWall):
    def __init__(self, width=BIG_WALL_LENGTH, height=BIG_WALL_LENGTH):
        super().__init__(width, height)
        self.type = UnitType.Asphalt
        self.health_points = ASPHALT_HEALTH_POINTS

    def on_explosion(self, field, explosion_rect: Rect):
        pass

    def is_intersected_with_unit(self, other: Unit) -> bool:
        return False

    def is_intersected_with_rect(self, rect: Unit) -> bool:
        return False
