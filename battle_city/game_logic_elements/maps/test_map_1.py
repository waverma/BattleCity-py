from battle_city.game_logic_elements.game_constants import LITTLE_WALL_LENGTH, \
    PLAYER_TANK_SPEED, PLAYER_TANK_HEALTH_POINTS, PLAYER_TANK_COOL_DOWN
from battle_city.game_logic_elements.game_field import GameField
from battle_city.game_logic_elements.units.armored_bot import ArmoredBot
from battle_city.game_logic_elements.units.asphalt import Asphalt
from battle_city.game_logic_elements.units.breakable_wall import BreakableWall
from battle_city.game_logic_elements.units.bush import Bush
from battle_city.game_logic_elements.units.dirt import Dirt
from battle_city.game_logic_elements.units.fire import Fire
from battle_city.game_logic_elements.units.heal_bot import HealBot
from battle_city.game_logic_elements.units.rapid_fire_bot import RapidFireBot
from battle_city.game_logic_elements.units.tank import Tank
from battle_city.game_logic_elements.units.tank_bot import TankBot
from battle_city.game_logic_elements.units.tank_bot_spawner import \
    TankBotSpawner
from battle_city.game_logic_elements.units.unbreakable_wall import \
    UnbreakableWall


def get_map() -> GameField:
    field = GameField()
    field.player = Tank()
    field.player.health_points = PLAYER_TANK_HEALTH_POINTS
    field.player.max_speed = PLAYER_TANK_SPEED
    field.player.shot_await_tick_count = PLAYER_TANK_COOL_DOWN
    field.try_place_unit(field.player, 0, 0)

    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 2,
        LITTLE_WALL_LENGTH * 2,
    )

    field.try_place_unit(
        UnbreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 4,
        LITTLE_WALL_LENGTH * 2,
    )

    field.try_place_unit(
        Bush(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 6,
        LITTLE_WALL_LENGTH * 2,
    )

    field.try_place_unit(
        Asphalt(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 12,
        LITTLE_WALL_LENGTH * 2,
    )

    spawner = TankBotSpawner(tank_to_go=4)
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(HealBot())
    spawner.tanks_to_go.append(RapidFireBot())
    field.try_place_unit(
        spawner,
        LITTLE_WALL_LENGTH * 10,
        LITTLE_WALL_LENGTH * 2,
    )

    field.try_place_unit(
        Fire(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 8,
        LITTLE_WALL_LENGTH * 2,
    )

    field.try_place_unit(
        Dirt(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 10,
        LITTLE_WALL_LENGTH * 2,
    )

    field.try_place_unit(
        ArmoredBot(),
        LITTLE_WALL_LENGTH * 17,
        LITTLE_WALL_LENGTH * 2,
    )

    field.try_place_unit(
        HealBot(),
        LITTLE_WALL_LENGTH * 19,
        LITTLE_WALL_LENGTH * 8,
    )

    field.try_place_unit(
        RapidFireBot(),
        LITTLE_WALL_LENGTH * 4,
        LITTLE_WALL_LENGTH * 17,
    )

    field.try_place_unit(
        TankBot(),
        LITTLE_WALL_LENGTH * 8,
        LITTLE_WALL_LENGTH * 17,
    )

    # field.units = field.units_buffer
    # field.units_buffer = list()

    return field
