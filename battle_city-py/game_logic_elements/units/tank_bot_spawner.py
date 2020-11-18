from pygame.rect import Rect

from enums.unit_type import UnitType
from enums.direction import Direction
from game_logic_elements.units.tank_bot import TankBot
from game_logic_elements.units.unit import Unit


class TankBotSpawner(Unit):
    def __init__(self):
        super().__init__()
        self.collision = Rect(-1, -1, 32, 32)
        self.is_tank_alive = False
        self.current_tank = None
        self.no_tank_tick_count = 70
        self.no_tank_tick_pointer = 0
        self.tank_to_go = 5
        self.type = UnitType.BotSpawner

    def step(self, field: 'GameField'):
        super().step(field)
        if not self.is_tank_alive:
            if self.no_tank_tick_pointer != self.no_tank_tick_count:
                self.no_tank_tick_pointer += 1
            else:
                self.no_tank_tick_pointer = 0
                self.current_tank = TankBot()
                self.current_tank.set_velocity(Direction.Down)
                if self.tank_to_go != 0 and field.try_place_unit(self.current_tank, self.collision.x, self.collision.y):
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
