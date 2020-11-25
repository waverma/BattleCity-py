from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.game_constants import HEAL_BOT_SPEED, \
    HEAL_TANK_SIZE, HEAL_TANK_COOL_DOWN, HEAL_TANK_HEALTH_POINTS, \
    HEAL_TANK_HEAL_COOL_DOWN
from battle_city.game_logic_elements.units.tank_bot import TankBot
from battle_city.rect import Rect


class HealBot(TankBot):
    def __init__(self):
        super().__init__()
        self.type = UnitType.TankGreenThree
        self.max_speed = HEAL_BOT_SPEED
        self.collision = Rect(-1, -1, HEAL_TANK_SIZE[0], HEAL_TANK_SIZE[1])
        self.shot_await_tick_count = HEAL_TANK_COOL_DOWN
        self.max_health_points = self.health_points = HEAL_TANK_HEALTH_POINTS
        self.heal_cool_dawn = HEAL_TANK_HEAL_COOL_DOWN
        self.heal_cool_dawn_pointer = 0

    def step(self, field):
        super().step(field)
        if self.heal_cool_dawn_pointer == self.heal_cool_dawn:
            if self.health_points < self.max_health_points:
                self.health_points += 1
        else:
            self.heal_cool_dawn_pointer += 1

    def on_shot(self, field, rect: Rect):
        super().on_shot(field, rect)
        self.heal_cool_dawn_pointer = 0
