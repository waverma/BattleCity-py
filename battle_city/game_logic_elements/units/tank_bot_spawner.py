from battle_city.enums.direction import Direction
from battle_city.enums.unit_type import UnitType
from battle_city.game_logic_elements.game_constants import \
    DEFAULT_TANK_SPAWNER_SIZE, DEFAULT_TANK_SPAWNER_COOL_DOWN, \
    DEFAULT_TANK_SPAWNER_TANK_TO_GO
from battle_city.game_logic_elements.units.tank_bot import TankBot
from battle_city.game_logic_elements.units.unit import Unit
from battle_city.rect import Rect


class TankBotSpawner(Unit):
    def __init__(self):
        super().__init__()
        self.collision = Rect(-1, -1, DEFAULT_TANK_SPAWNER_SIZE[0], DEFAULT_TANK_SPAWNER_SIZE[1])
        self.is_tank_alive = False
        self.current_tank = None
        self.no_tank_tick_count = DEFAULT_TANK_SPAWNER_COOL_DOWN
        self.no_tank_tick_pointer = 0
        self.tank_to_go = DEFAULT_TANK_SPAWNER_TANK_TO_GO
        self.type = UnitType.BotSpawner

    def step(self, field):
        super().step(field)
        if not self.is_tank_alive:
            if self.no_tank_tick_pointer != self.no_tank_tick_count:
                self.no_tank_tick_pointer += 1
            else:
                self.no_tank_tick_pointer = 0
                self.current_tank = TankBot()
                self.current_tank.set_velocity(Direction.Down)
                if self.tank_to_go != 0 and field.try_place_unit(
                    self.current_tank, self.collision.x, self.collision.y
                ):
                    self.tank_to_go -= 1
                self.is_tank_alive = True
        else:
            if self.current_tank not in field.units:
                self.is_tank_alive = False
                self.current_tank = None

    def is_intersected_with_unit(self, other: Unit) -> bool:
        return False

    def is_intersected_with_rect(self, rect: Unit) -> bool:
        return False
