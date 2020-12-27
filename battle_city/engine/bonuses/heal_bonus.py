from battle_city.enums import UnitType
from battle_city.engine.game_constants import BONUS_HEAL_VALUE
from battle_city.engine.bonuses.unit_upgrade import UnitBonus


class HealBonus(UnitBonus):
    def __init__(self):
        super().__init__()
        self.type = UnitType.HealBonus

    def on_update_action(self):
        self.owner.health_points += BONUS_HEAL_VALUE
        self.tick_pointer = self.action_duration * 2
