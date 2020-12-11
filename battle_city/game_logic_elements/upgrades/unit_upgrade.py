from battle_city.enums import UnitType
from battle_city.game_logic_elements.game_constants import BONUS_DURATION
from battle_city.game_logic_elements.units.tank import Tank


class UnitUpgrade:
    def __init__(self):
        self.owner: Tank = None
        self.type = UnitType.HealBonus
        self.action_duration = BONUS_DURATION
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
        pass

    def turn_on(self):
        self.is_active = True
        self.owner.current_bonus = self

    def turn_off(self):
        self.is_active = False
        self.owner.current_bonus = None
