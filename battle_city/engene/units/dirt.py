from battle_city.enums import UnitType, UpdateMode
from battle_city.engene.game_constants import (
    BIG_WALL_LENGTH,
    DIRT_HEALTH_POINTS,
    DIRT_SLOW_DAWN_COEFFICIENT,
)
from battle_city.engene.units.breakable_wall import BreakableWall
from battle_city.engene.units.tank import Tank
from battle_city.engene.units.unit import Unit


class Dirt(BreakableWall):
    def __init__(self, width=BIG_WALL_LENGTH, height=BIG_WALL_LENGTH):
        super().__init__(width, height)
        self.type = UnitType.Dirt
        self.health_points = DIRT_HEALTH_POINTS
        self.update_mode = UpdateMode.StepOnly
        self.intersected_tanks = list()

    def step(self, field):
        for tank in self.intersected_tanks:
            tank[0].max_speed = tank[1]
            tank[0].set_velocity(tank[0].current_move_direction)
        self.intersected_tanks = list()

        for unit in field.get_intersected_units(self.collision):
            if issubclass(type(unit), Tank):
                self.intersected_tanks.append((unit, unit.max_speed))
                unit.max_speed = int(
                    unit.max_speed / DIRT_SLOW_DAWN_COEFFICIENT
                )
                if unit.max_speed == 0:
                    unit.max_speed = 1
                unit.set_velocity(unit.current_move_direction)

    def is_intersected_with_unit(self, other: Unit) -> bool:
        return False

    def is_intersected_with_rect(self, rect: Unit) -> bool:
        return False
