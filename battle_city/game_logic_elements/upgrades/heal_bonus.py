from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.game_constants import BONUS_HEAL_VALUE
from battle_city.game_logic_elements.upgrades.unit_upgrade import UnitUpgrade


class HealBonus(UnitUpgrade):
    def __init__(self):
        super().__init__()
        self.type = UnitType.HealBonus

    def on_update_action(self):
        self.owner.health_points += BONUS_HEAL_VALUE
        self.tick_pointer = self.action_duration * 2
