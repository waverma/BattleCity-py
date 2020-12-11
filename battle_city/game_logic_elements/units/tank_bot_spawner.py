import random

from battle_city.enums import Direction
from battle_city.enums import UnitType
from battle_city.enums import UpdateMode
from battle_city.game_logic_elements.game_constants import \
    DEFAULT_TANK_SPAWNER_SIZE, DEFAULT_TANK_SPAWNER_COOL_DOWN, \
    DEFAULT_TANK_SPAWNER_TANK_TO_GO
from battle_city.game_logic_elements.units.tank_bot import TankBot
from battle_city.game_logic_elements.units.unit import Unit
from battle_city.rect import Rect


class TankBotSpawner(Unit):
    def __init__(
            self,
            tank_to_go=DEFAULT_TANK_SPAWNER_TANK_TO_GO,
            next_tank_pointer=None,
            priority_direction=None
    ):
        super().__init__()
        self.collision = Rect(-1, -1, DEFAULT_TANK_SPAWNER_SIZE[0],
                              DEFAULT_TANK_SPAWNER_SIZE[1])
        self.type = UnitType.BotSpawner

        self.is_tank_alive = False
        self.current_tank = None
        self.no_tank_tick_count = DEFAULT_TANK_SPAWNER_COOL_DOWN
        self.no_tank_tick_pointer = 0

        self.tank_to_go = tank_to_go
        self.next_tank_pointer = next_tank_pointer
        self.tanks_to_go = list()
        self.priority_direction = priority_direction

        self.update_mode = UpdateMode.StepOnly

        self.directions = [
            Direction.Down,
            Direction.Up,
            Direction.Right,
            Direction.Left,
        ]

    def is_completed(self) -> bool:
        return (self.tank_to_go <= 0
                or len(self.tanks_to_go) <= 0
                or (self.next_tank_pointer is not None and self.next_tank_pointer >= len(self.tanks_to_go))) \
               and self.is_tank_alive

    def get_next_tank(self) -> TankBot:
        if self.next_tank_pointer is None:
            if len(self.tanks_to_go) > 1:
                tank_number = random.randint(0, len(self.tanks_to_go) - 1)
            else:
                tank_number = 0
            if tank_number >= len(self.tanks_to_go):
                return None
            tank = self.tanks_to_go[tank_number]
            self.tanks_to_go.remove(tank)
        else:
            if self.next_tank_pointer >= len(self.tanks_to_go):
                return None
            tank = self.tanks_to_go[self.next_tank_pointer]
            self.next_tank_pointer += 1

        if self.priority_direction is None:
            tank.set_velocity(self.directions[random.randint(0, 3)])
        else:
            tank.set_velocity(self.priority_direction)

        if self.is_completed:
            self.type = UnitType.BotSpawner

        return tank

    def step(self, field):
        super().step(field)
        if not self.is_tank_alive:
            if self.no_tank_tick_pointer != self.no_tank_tick_count:
                self.no_tank_tick_pointer += 1
            else:
                self.no_tank_tick_pointer = 0
                self.current_tank = self.get_next_tank()
                if self.current_tank is None:
                    self.type = UnitType.EmptyBotSpawner
                elif field.try_place_unit(
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
