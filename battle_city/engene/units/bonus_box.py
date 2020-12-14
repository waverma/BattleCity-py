from battle_city.enums import UnitType
from battle_city.engene.game_constants import (
    BONUS_COOL_DOWN,
    LITTLE_WALL_LENGTH,
    ONLY_PLAYER_MODE,
)
from battle_city.engene.units.tank import Tank
from battle_city.engene.units.unit import Unit
from battle_city.rect import Rect


class BonusBox(Unit):
    def __init__(self):
        super().__init__()
        self.bonuses = list()
        self.next_bonuses = None
        self.type = UnitType.BonusSpawner
        self.cool_down = BONUS_COOL_DOWN
        self.tick_pointer = 0
        self.collision = Rect(w=LITTLE_WALL_LENGTH, h=LITTLE_WALL_LENGTH)

    def step(self, field):
        super().step(field)

        steel_bonuses = list()
        for bonus in self.bonuses:
            bonus.update()
            if bonus.is_active:
                steel_bonuses.append(bonus)
        self.bonuses = steel_bonuses

        self.tick_pointer += 1
        if self.tick_pointer >= self.cool_down:
            for unit in field.get_intersected_units(self.collision):
                if (
                    (ONLY_PLAYER_MODE and field.player is unit)
                    or (not ONLY_PLAYER_MODE and issubclass(type(unit), Tank))
                ) and unit.current_bonus is None:
                    new_bonus = self.next_bonuses()
                    new_bonus.owner = unit
                    self.bonuses.append(new_bonus)
                    new_bonus.turn_on()

                    self.tick_pointer = 0
                    break

    def on_explosion(self, field, explosion_rect: Rect):
        pass

    def is_intersected_with_unit(self, other: Unit) -> bool:
        return False

    def is_intersected_with_rect(self, rect: Unit) -> bool:
        return False

    def get_render_info(self) -> list:
        result = []
        if (
            self.next_bonuses is not None
            and self.tick_pointer >= self.cool_down
        ):
            result.append(
                (
                    self.next_bonuses().type,
                    self.collision,
                    self.current_direction,
                )
            )
        return result
