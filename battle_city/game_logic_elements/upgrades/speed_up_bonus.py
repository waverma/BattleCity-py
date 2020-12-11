from battle_city.enums import UnitType
from battle_city.game_logic_elements.upgrades.unit_upgrade import UnitUpgrade


class SpeedUpBonus(UnitUpgrade):
    def __init__(self):
        super().__init__()
        self.type = UnitType.SpeedUpBonus
        self.saved_max_speed = 0

    def turn_on(self):
        super().turn_on()
        self.saved_max_speed = self.owner.max_speed
        self.owner.max_speed = self.owner.max_speed * 2

    def turn_off(self):
        super().turn_off()
        self.owner.max_speed = self.saved_max_speed
