from pygame import Rect

from enums.tank_texture_kind import TankTextureKind
from game_logic_elements.units.breakable_wall import BreakableWall
from game_logic_elements.units.bullet import Bullet
from game_logic_elements.units.tank import Tank
from game_logic_elements.units.tank_bot import TankBot
from game_logic_elements.units.tank_bot_spawner import TankBotSpawner
from game_logic_elements.units.unbreakable_wall import UnbreakableWall
from game_logic_elements.units.unit import Unit


class GameField:
    def __init__(self):
        self.width = self.height = 26 * 20

        self.player = Tank(TankTextureKind.Orange)
        self.player.color = (0, 255, 255)
        self.player.health_points = self.player.health_points = 1
        self.units = list()
        self.spawners = list()
        self.units_buffer = list()
        self.ban_unit_list = list()
        self.try_place_unit(self.player, 0, 0)
        self.set_game_field()

        self.game = None

    def update(self):
        self.units_buffer = list(self.units)
        for unit in self.units:
            if unit not in self.ban_unit_list:
                unit.step(self)

        self.units = self.units_buffer
        self.units_buffer = list()

        for unit in self.ban_unit_list:
            if unit in self.units:
                self.units.remove(unit)
        self.ban_unit_list = list()

    def set_game_field(self):
        cell_len = 20

        # стены
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 9), cell_len * 2, cell_len * 2)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 9), cell_len * 6, cell_len * 2)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 9), cell_len * 18, cell_len * 2)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 9), cell_len * 22, cell_len * 2)

        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 7), cell_len * 10, cell_len * 2)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 7), cell_len * 14, cell_len * 2)

        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 7), cell_len * 2, cell_len * 17)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 7), cell_len * 6, cell_len * 17)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 7), cell_len * 18, cell_len * 17)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 7), cell_len * 22, cell_len * 17)

        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 6), cell_len * 10, cell_len * 15)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 6), cell_len * 14, cell_len * 15)

        self.try_place_unit(BreakableWall(cell_len * 4, cell_len * 2), cell_len * 4, cell_len * 13)
        self.try_place_unit(BreakableWall(cell_len * 4, cell_len * 2), cell_len * 18, cell_len * 13)

        self.try_place_unit(BreakableWall(cell_len * 2, cell_len), 0, cell_len * 13)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len), cell_len * 24, cell_len * 13)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 2), cell_len * 10, cell_len * 11)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 2), cell_len * 14, cell_len * 11)
        self.try_place_unit(UnbreakableWall(cell_len * 2, cell_len * 2), cell_len * 12, cell_len * 6)
        self.try_place_unit(BreakableWall(cell_len * 2, cell_len * 2), cell_len * 12, cell_len * 16)

        self.try_place_unit(UnbreakableWall(cell_len * 2, cell_len), 0, cell_len * 14)
        self.try_place_unit(UnbreakableWall(cell_len * 2, cell_len), cell_len * 24, cell_len * 14)

        # враги
        spawner = TankBotSpawner()
        self.spawners.append(spawner)
        self.try_place_unit(spawner, cell_len * 24 + 2, 0)

        spawner = TankBotSpawner()
        self.try_place_unit(spawner, cell_len * 8 + 2, cell_len * 11)
        self.spawners.append(spawner)

        spawner = TankBotSpawner()
        self.try_place_unit(spawner, cell_len * 12 + 2, cell_len * 18)
        self.spawners.append(spawner)

        self.units = self.units_buffer
        self.units_buffer = list()

    def try_place_unit(self, unit: Unit, x: int, y: int):
        rect = Rect(x, y, unit.collision.width, unit.collision.height)
        if not Rect(0, 0, self.width, self.height).collidepoint(x, y) \
                or not Rect(0, 0, self.width, self.height).collidepoint(x + unit.collision.width - 1, y + unit.collision.height - 1) \
                or len(self.get_intersected_units(rect)) > 0:
            return False

        unit.collision.x = x
        unit.collision.y = y
        self.units_buffer.append(unit)
        return True

    def try_remove_unit(self, unit: Unit) -> bool:
        saved_length = len(self.units_buffer)
        if unit in self.units_buffer:
            self.units_buffer.remove(unit)
        else:
            self.ban_unit_list.append(unit)
        return saved_length != len(self.units_buffer)

    def get_intersected_units(self, rect: Rect) -> list:
        result = list()

        for unit in self.units_buffer:
            if unit.is_intersected_with_rect(rect):
                result.append(unit)

        return result

    def explode(self, source_explosion: Bullet, radius: int, source_rect: Rect, collide_units: list = None):
        explosion_rect = Rect(
            source_rect.x + source_rect.width / 2 - radius / 2,
            source_rect.y + source_rect.height / 2 - radius / 2,
            radius,
            radius
        )

        if collide_units is None:
            for unit in self.get_intersected_units(explosion_rect):
                unit.on_explosion(self, explosion_rect)
        else:
            for unit in self.get_intersected_units(explosion_rect):
                if unit not in collide_units:
                    unit.on_explosion(self, explosion_rect)
                else:
                    unit.on_shot(self, explosion_rect)
                    if type(unit) is TankBot \
                            and unit not in self.units_buffer \
                            and source_explosion.owner is self.player \
                            and self.game is not None:
                        self.game.points += 1
