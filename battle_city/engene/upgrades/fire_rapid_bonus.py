from battle_city.enums import UnitType
from battle_city.engene.upgrades.unit_upgrade import UnitUpgrade


class FireRapidBonus(UnitUpgrade):
    def __init__(self):
        super().__init__()
        self.type = UnitType.CoolDownBonus
        self.saved_cool_down = 0

    def turn_on(self):
        super().turn_on()
        self.saved_cool_down = self.owner.shot_await_tick_count
        self.owner.shot_await_tick_count = (
            self.owner.shot_await_tick_count // 2
        )

    def turn_off(self):
        super().turn_off()
        self.owner.shot_await_tick_count = self.saved_cool_down
