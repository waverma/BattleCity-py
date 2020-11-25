from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.game_constants import ARMORED_BOT_SPEED, \
    ARMORED_TANK_SIZE, ARMORED_TANK_COOL_DOWN, ARMORED_TANK_HEALTH_POINTS
from battle_city.game_logic_elements.units.tank_bot import TankBot
from battle_city.rect import Rect


class ArmoredBot(TankBot):
    def __init__(self):
        super().__init__()
        self.type = UnitType.TankRed
        self.max_speed = ARMORED_BOT_SPEED
        self.collision = Rect(-1, -1, ARMORED_TANK_SIZE[0], ARMORED_TANK_SIZE[1])
        self.shot_await_tick_count = ARMORED_TANK_COOL_DOWN
        self.health_points = ARMORED_TANK_HEALTH_POINTS
