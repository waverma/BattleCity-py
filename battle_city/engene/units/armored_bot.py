from battle_city.enums import UnitType
from battle_city.engene.game_constants import (
    ARMORED_BOT_SPEED,
    ARMORED_TANK_COOL_DOWN,
    ARMORED_TANK_HEALTH_POINTS,
    ARMORED_TANK_SIZE,
)
from battle_city.engene.units.tank_bot import TankBot
from battle_city.rect import Rect


class ArmoredBot(TankBot):
    def __init__(self):
        super().__init__()
        self.type = UnitType.TankRed
        self.max_speed = ARMORED_BOT_SPEED
        self.collision = Rect(w=ARMORED_TANK_SIZE[0], h=ARMORED_TANK_SIZE[1])
        self.shot_await_tick_count = ARMORED_TANK_COOL_DOWN
        self.health_points = ARMORED_TANK_HEALTH_POINTS
