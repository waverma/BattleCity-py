from battle_city.enums import UnitType, UpdateMode
from battle_city.engine.game_constants import (
    DEFAULT_GAME_FIELD_SIZE,
)
from battle_city.engine.units.bullet import Bullet
from battle_city.engine.units.unit import Unit
from battle_city.rect import Rect


class GameField:
    player: Unit

    def __init__(self):
        self.width = self.height = DEFAULT_GAME_FIELD_SIZE[0]
        self.spawners = list()

        self.units_for_step = list()
        self.units_for_step_buffer = list()
        self.units_for_intersect = list()
        self.units_for_intersect_buffer = list()

        self.units = list()
        self.ban_unit_list = list()

        self.game = None

    def update(self):
        self.units_for_step_buffer = list(self.units_for_step)
        self.units_for_intersect_buffer = list(self.units_for_intersect)

        for unit in self.units_for_step:
            if unit not in self.ban_unit_list:
                unit.step(self)

        self.units_for_step = self.units_for_step_buffer
        self.units_for_intersect = self.units_for_intersect_buffer

        self.units_for_step_buffer = list()
        self.units_for_intersect_buffer = list()

        for unit in self.ban_unit_list:
            if unit in self.units:
                self.units.remove(unit)
                if unit.update_mode == UpdateMode.IntersectOnly:
                    self.units_for_intersect.remove(unit)
                if unit.update_mode == UpdateMode.StepOnly:
                    self.units_for_step.remove(unit)
                if unit.update_mode == UpdateMode.StepIntersect:
                    self.units_for_intersect.remove(unit)
                    self.units_for_step.remove(unit)
        self.ban_unit_list = list()

    def try_place_unit(
            self, unit: Unit, x: int, y: int, non_intersect_mode: bool = False
    ):
        unit_rect = Rect(x, y, unit.collision.width, unit.collision.height)
        map_rect = Rect(0, 0, self.width, self.height)
        if (
            not map_rect.collidepoint(x, y)
            or not map_rect.collidepoint(
                x + unit.collision.width - 1, y + unit.collision.height - 1
            )
            or len(self.get_intersected_units(unit_rect)) > 0
        ) and not non_intersect_mode:
            return False

        unit.collision.set_x(x).set_y(y)
        self.units.append(unit)
        if unit.update_mode == UpdateMode.IntersectOnly:
            self.units_for_intersect_buffer.append(unit)
        elif unit.update_mode == UpdateMode.StepOnly:
            self.units_for_step_buffer.append(unit)
        elif unit.update_mode == UpdateMode.StepIntersect:
            self.units_for_intersect_buffer.append(unit)
            self.units_for_step_buffer.append(unit)

        return True

    def try_remove_unit(self, unit: Unit) -> bool:
        saved_length = len(self.units)
        if unit in self.units:
            self.units.remove(unit)
            if unit.update_mode == UpdateMode.IntersectOnly:
                self.units_for_intersect_buffer.remove(unit)
            if unit.update_mode == UpdateMode.StepOnly:
                self.units_for_step_buffer.remove(unit)
            if unit.update_mode == UpdateMode.StepIntersect:
                self.units_for_intersect_buffer.remove(unit)
                self.units_for_step_buffer.remove(unit)
        else:
            self.ban_unit_list.append(unit)

        return saved_length != len(self.units)

    def get_intersected_units(self, rect: Rect) -> list:
        result = list()

        for unit in self.units_for_intersect_buffer:
            if unit.is_intersected_with_rect(rect):
                result.append(unit)

        return result

    def explode(
        self,
        source_explosion: Bullet,
        radius: int,
        source_rect: Rect,
        collide_units: list = None,
    ):
        explosion_rect = Rect(
            int(source_rect.x + source_rect.width / 2 - radius / 2),
            int(source_rect.y + source_rect.height / 2 - radius / 2),
            radius,
            radius,
        )

        if collide_units is None:
            for unit in self.get_intersected_units(explosion_rect):
                unit.on_explosion(self, explosion_rect)
                self.try_set_score(unit, source_explosion.owner)
        else:
            for unit in self.get_intersected_units(explosion_rect):
                if unit not in collide_units:
                    unit.on_explosion(self, explosion_rect)
                else:
                    unit.on_shot(self, explosion_rect)
                self.try_set_score(unit, source_explosion.owner)

    def try_set_score(self, unit: Unit, owner: Unit):
        if unit in self.units or owner is not self.player or self.game is None:
            return

        if unit.type == UnitType.TankWhite:
            self.game.tank_bot_kills += 1
            self.game.kills += 1
        elif unit.type == UnitType.TankRed:
            self.game.armored_bot_kills += 1
            self.game.kills += 1
        elif unit.type == UnitType.TankOrange:
            self.game.rapid_fire_kills += 1
            self.game.kills += 1
        elif unit.type == UnitType.TankGreenThree:
            self.game.heal_bot_kills += 1
            self.game.kills += 1
