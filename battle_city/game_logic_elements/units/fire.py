from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.game_constants import FIRE_HEALTH_POINTS, \
    FIRE_DAMAGE_COOL_DOWN
from battle_city.game_logic_elements.units.breakable_wall import BreakableWall
from battle_city.game_logic_elements.units.tank import Tank
from battle_city.game_logic_elements.units.unit import Unit
from battle_city.rect import Rect


class Fire(BreakableWall):
    def __init__(self):
        super().__init__()
        self.type = UnitType.Fire
        self.health_points = FIRE_HEALTH_POINTS

        self.damage_cool_down = FIRE_DAMAGE_COOL_DOWN
        self.damage_cool_down_pointer = 0

    def step(self, field):
        super().step(field)

        if self.damage_cool_down_pointer >= self.damage_cool_down:
            for unit in field.get_intersected_units(self.collision):
                if type(unit) is Tank:
                    unit.on_shot(field)
            self.damage_cool_down_pointer = 0
        else:
            self.damage_cool_down_pointer += 1

    def on_explosion(self, field, explosion_rect: Rect):
        pass

    def is_intersected_with_unit(self, other: Unit) -> bool:
        return False

    def is_intersected_with_rect(self, rect: Unit) -> bool:
        return False
