from battle_city.game_logic_elements.game_constants import \
    DEFAULT_GAME_FIELD_SIZE, LITTLE_WALL_LENGTH, PLAYER_TANK_HEALTH_POINTS, \
    PLAYER_TANK_SPEED, PLAYER_TANK_COOL_DOWN
from battle_city.game_logic_elements.units.armored_bot import ArmoredBot
from battle_city.game_logic_elements.units.asphalt import Asphalt
from battle_city.game_logic_elements.units.breakable_wall import BreakableWall
from battle_city.game_logic_elements.units.bullet import Bullet
from battle_city.game_logic_elements.units.bush import Bush
from battle_city.game_logic_elements.units.dirt import Dirt
from battle_city.game_logic_elements.units.fire import Fire
from battle_city.game_logic_elements.units.heal_bot import HealBot
from battle_city.game_logic_elements.units.rapid_fire_bot import RapidFireBot
from battle_city.game_logic_elements.units.tank import Tank
from battle_city.game_logic_elements.units.tank_bot import TankBot
from battle_city.game_logic_elements.units.tank_bot_spawner import TankBotSpawner
from battle_city.game_logic_elements.units.unbreakable_wall import UnbreakableWall
from battle_city.game_logic_elements.units.unit import Unit
from battle_city.rect import Rect


class GameField:
    player: Unit

    def __init__(self):
        self.width = self.height = DEFAULT_GAME_FIELD_SIZE[0]

        self.units = list()
        self.spawners = list()
        self.units_buffer = list()
        self.ban_unit_list = list()

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

    def set_test_game_field(self):
        self.player = Tank()
        self.player.health_points = PLAYER_TANK_HEALTH_POINTS
        self.player.max_speed = PLAYER_TANK_SPEED
        self.player.shot_await_tick_count = PLAYER_TANK_COOL_DOWN
        self.try_place_unit(self.player, 0, 0)

        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 2,
            LITTLE_WALL_LENGTH * 2,
        )

        self.try_place_unit(
            UnbreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 4,
            LITTLE_WALL_LENGTH * 2,
        )

        self.try_place_unit(
            Bush(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 6,
            LITTLE_WALL_LENGTH * 2,
        )

        self.try_place_unit(
            Asphalt(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 12,
            LITTLE_WALL_LENGTH * 2,
        )

        spawner = TankBotSpawner(tank_to_go=5)
        spawner.tanks_to_go.append(TankBot())
        spawner.tanks_to_go.append(ArmoredBot())
        spawner.tanks_to_go.append(HealBot())
        spawner.tanks_to_go.append(RapidFireBot())
        self.try_place_unit(
            spawner,
            LITTLE_WALL_LENGTH * 10,
            LITTLE_WALL_LENGTH * 2,
        )

        self.try_place_unit(
            Fire(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 8,
            LITTLE_WALL_LENGTH * 2,
        )

        self.try_place_unit(
            Dirt(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 10,
            LITTLE_WALL_LENGTH * 2,
        )

        self.try_place_unit(
            ArmoredBot(),
            LITTLE_WALL_LENGTH * 17,
            LITTLE_WALL_LENGTH * 2,
        )

        self.try_place_unit(
            HealBot(),
            LITTLE_WALL_LENGTH * 19,
            LITTLE_WALL_LENGTH * 8,
        )

        self.try_place_unit(
            RapidFireBot(),
            LITTLE_WALL_LENGTH * 4,
            LITTLE_WALL_LENGTH * 17,
        )

        self.try_place_unit(
            TankBot(),
            LITTLE_WALL_LENGTH * 8,
            LITTLE_WALL_LENGTH * 17,
        )

        self.units = self.units_buffer
        self.units_buffer = list()

    def set_game_field(self):
        self.player = Tank()
        self.player.health_points = PLAYER_TANK_HEALTH_POINTS
        self.player.max_speed = PLAYER_TANK_SPEED
        self.player.shot_await_tick_count = PLAYER_TANK_COOL_DOWN
        self.try_place_unit(self.player, 0, 0)

        # стены
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 2,
            LITTLE_WALL_LENGTH * 2,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 6,
            LITTLE_WALL_LENGTH * 2,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 18,
            LITTLE_WALL_LENGTH * 2,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
            LITTLE_WALL_LENGTH * 22,
            LITTLE_WALL_LENGTH * 2,
        )

        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
            LITTLE_WALL_LENGTH * 10,
            LITTLE_WALL_LENGTH * 2,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
            LITTLE_WALL_LENGTH * 14,
            LITTLE_WALL_LENGTH * 2,
        )

        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
            LITTLE_WALL_LENGTH * 2,
            LITTLE_WALL_LENGTH * 17,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
            LITTLE_WALL_LENGTH * 6,
            LITTLE_WALL_LENGTH * 17,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
            LITTLE_WALL_LENGTH * 18,
            LITTLE_WALL_LENGTH * 17,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
            LITTLE_WALL_LENGTH * 22,
            LITTLE_WALL_LENGTH * 17,
        )

        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 6),
            LITTLE_WALL_LENGTH * 10,
            LITTLE_WALL_LENGTH * 15,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 6),
            LITTLE_WALL_LENGTH * 14,
            LITTLE_WALL_LENGTH * 15,
        )

        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 4, LITTLE_WALL_LENGTH * 2),
            LITTLE_WALL_LENGTH * 4,
            LITTLE_WALL_LENGTH * 13,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 4, LITTLE_WALL_LENGTH * 2),
            LITTLE_WALL_LENGTH * 18,
            LITTLE_WALL_LENGTH * 13,
        )

        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH), 0, LITTLE_WALL_LENGTH * 13
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH), LITTLE_WALL_LENGTH * 24, LITTLE_WALL_LENGTH * 13
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 2),
            LITTLE_WALL_LENGTH * 10,
            LITTLE_WALL_LENGTH * 11,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 2),
            LITTLE_WALL_LENGTH * 14,
            LITTLE_WALL_LENGTH * 11,
        )
        self.try_place_unit(
            UnbreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 2),
            LITTLE_WALL_LENGTH * 12,
            LITTLE_WALL_LENGTH * 6,
        )
        self.try_place_unit(
            BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 2),
            LITTLE_WALL_LENGTH * 12,
            LITTLE_WALL_LENGTH * 16,
        )

        self.try_place_unit(
            UnbreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH), 0, LITTLE_WALL_LENGTH * 14
        )
        self.try_place_unit(
            UnbreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH),
            LITTLE_WALL_LENGTH * 24,
            LITTLE_WALL_LENGTH * 14,
        )

        # враги
        spawner = TankBotSpawner()
        self.spawners.append(spawner)
        self.try_place_unit(spawner, LITTLE_WALL_LENGTH * 24, 0)

        spawner = TankBotSpawner()
        self.try_place_unit(spawner, LITTLE_WALL_LENGTH * 8, LITTLE_WALL_LENGTH * 11)
        self.spawners.append(spawner)

        spawner = TankBotSpawner()
        self.try_place_unit(spawner, LITTLE_WALL_LENGTH * 12, LITTLE_WALL_LENGTH * 18)
        self.spawners.append(spawner)

        self.units = self.units_buffer
        self.units_buffer = list()

    def try_place_unit(self, unit: Unit, x: int, y: int):
        unit_rect = Rect(x, y, unit.collision.width, unit.collision.height)
        map_rect = Rect(0, 0, self.width, self.height)
        if (
            not map_rect.collidepoint(x, y)
            or not map_rect.collidepoint(
                x + unit.collision.width - 1, y + unit.collision.height - 1
            )
            or len(self.get_intersected_units(unit_rect)) > 0
        ):
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
        else:
            for unit in self.get_intersected_units(explosion_rect):
                if unit not in collide_units:
                    unit.on_explosion(self, explosion_rect)
                else:
                    unit.on_shot(self, explosion_rect)
                    if (
                        type(unit) is TankBot
                        and unit not in self.units_buffer
                        and source_explosion.owner is self.player
                        and self.game is not None
                    ):
                        self.game.score += 1
