from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.units.unit import Unit


class UnitUpgrade:
    def __init__(self):
        self.owner: Unit = None
        self.type = UnitType.HealBonus
        self.action_duration = 1000
        self.tick_pointer = 0
        self.is_active = False

    def update(self):
        if not self.is_active:
            return
        
        self.on_update_action()

        self.tick_pointer += 1
        if self.tick_pointer >= self.action_duration:
            self.tick_pointer = 0
            self.turn_off()

    def on_update_action(self):
        self.owner.health_points += 5
        self.tick_pointer = self.action_duration * 2

    def turn_on(self):
        self.is_active = True

    def turn_off(self):
        self.is_active = False
