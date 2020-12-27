from battle_city.enums import UnitType
from battle_city.engine.game_constants import (
    RAPID_FIRE_BOT_SPEED,
    RAPID_FIRE_TANK_COOL_DOWN,
    RAPID_FIRE_TANK_HEALTH_POINTS,
    RAPID_FIRE_TANK_SIZE,
)
from battle_city.engine.units.tank_bot import TankBot
from battle_city.rect import Rect


class RapidFireBot(TankBot):
    def __init__(self):
        super().__init__()
        self.type = UnitType.TankOrange
        self.max_speed = RAPID_FIRE_BOT_SPEED
        self.collision = Rect(
            w=RAPID_FIRE_TANK_SIZE[0], h=RAPID_FIRE_TANK_SIZE[1]
        )
        self.shot_await_tick_count = RAPID_FIRE_TANK_COOL_DOWN
        self.health_points = RAPID_FIRE_TANK_HEALTH_POINTS
