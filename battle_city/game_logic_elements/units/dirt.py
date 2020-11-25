from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.game_constants import DIRT_HEALTH_POINTS, \
    DIRT_SLOW_DAWN_COEFFICIENT
from battle_city.game_logic_elements.units.breakable_wall import BreakableWall
from battle_city.game_logic_elements.units.tank import Tank
from battle_city.game_logic_elements.units.unit import Unit
from battle_city.rect import Rect


class Dirt(BreakableWall):
    def __init__(self):
        super().__init__()
        self.type = UnitType.Dirt
        self.health_points = DIRT_HEALTH_POINTS

        self.intersected_tanks = list()

    def on_explosion(self, field, explosion_rect: Rect):
        for tank in self.intersected_tanks:
            tank[0].max_speed = tank[1]
        self.intersected_tanks = list()

        for unit in field.get_intersected_units(self.collision):
            if type(unit) is Tank:
                self.intersected_tanks.append((unit, unit.max_speed))
                unit.max_speed = int(unit.max_speed
                                     / DIRT_SLOW_DAWN_COEFFICIENT)

    def is_intersected_with_unit(self, other: Unit) -> bool:
        return False

    def is_intersected_with_rect(self, rect: Unit) -> bool:
        return False
