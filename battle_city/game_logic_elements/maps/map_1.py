from battle_city.game_logic_elements.game_constants import \
    PLAYER_TANK_HEALTH_POINTS, PLAYER_TANK_SPEED, PLAYER_TANK_COOL_DOWN, \
    LITTLE_WALL_LENGTH, BIG_WALL_LENGTH
from battle_city.game_logic_elements.game_field import GameField
from battle_city.game_logic_elements.units.armored_bot import ArmoredBot
from battle_city.game_logic_elements.units.asphalt import Asphalt
from battle_city.game_logic_elements.units.bonus_box import BonusBox
from battle_city.game_logic_elements.units.breakable_wall import BreakableWall
from battle_city.game_logic_elements.units.tank import Tank
from battle_city.game_logic_elements.units.tank_bot import TankBot
from battle_city.game_logic_elements.units.tank_bot_spawner import \
    TankBotSpawner
from battle_city.game_logic_elements.units.unbreakable_wall import \
    UnbreakableWall
from battle_city.game_logic_elements.upgrades.fire_rapid_bonus import \
    FireRapidBonus


def get_map() -> GameField:
    field = GameField()

    field.try_place_unit(
        Asphalt(LITTLE_WALL_LENGTH * 26, LITTLE_WALL_LENGTH * 26), 0, 0,
    )

    field.player = Tank()
    field.player.health_points = PLAYER_TANK_HEALTH_POINTS
    field.player.max_speed = PLAYER_TANK_SPEED
    field.player.shot_await_tick_count = PLAYER_TANK_COOL_DOWN
    field.try_place_unit(field.player, 0, 0)

    # стены
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 2,
        LITTLE_WALL_LENGTH * 2,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 6,
        LITTLE_WALL_LENGTH * 2,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 18,
        LITTLE_WALL_LENGTH * 2,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 9),
        LITTLE_WALL_LENGTH * 22,
        LITTLE_WALL_LENGTH * 2,
    )

    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
        LITTLE_WALL_LENGTH * 10,
        LITTLE_WALL_LENGTH * 2,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
        LITTLE_WALL_LENGTH * 14,
        LITTLE_WALL_LENGTH * 2,
    )

    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
        LITTLE_WALL_LENGTH * 2,
        LITTLE_WALL_LENGTH * 17,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
        LITTLE_WALL_LENGTH * 6,
        LITTLE_WALL_LENGTH * 17,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
        LITTLE_WALL_LENGTH * 18,
        LITTLE_WALL_LENGTH * 17,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 7),
        LITTLE_WALL_LENGTH * 22,
        LITTLE_WALL_LENGTH * 17,
    )

    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 6),
        LITTLE_WALL_LENGTH * 10,
        LITTLE_WALL_LENGTH * 15,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 6),
        LITTLE_WALL_LENGTH * 14,
        LITTLE_WALL_LENGTH * 15,
    )

    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 4, LITTLE_WALL_LENGTH * 2),
        LITTLE_WALL_LENGTH * 4,
        LITTLE_WALL_LENGTH * 13,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 4, LITTLE_WALL_LENGTH * 2),
        LITTLE_WALL_LENGTH * 18,
        LITTLE_WALL_LENGTH * 13,
    )

    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH), 0,
        LITTLE_WALL_LENGTH * 13
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH),
        LITTLE_WALL_LENGTH * 24, LITTLE_WALL_LENGTH * 13
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 2),
        LITTLE_WALL_LENGTH * 10,
        LITTLE_WALL_LENGTH * 11,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 2),
        LITTLE_WALL_LENGTH * 14,
        LITTLE_WALL_LENGTH * 11,
    )
    field.try_place_unit(
        UnbreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 2),
        LITTLE_WALL_LENGTH * 12,
        LITTLE_WALL_LENGTH * 6,
    )
    field.try_place_unit(
        BreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH * 2),
        LITTLE_WALL_LENGTH * 12,
        LITTLE_WALL_LENGTH * 16,
    )

    field.try_place_unit(
        UnbreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH), 0,
        LITTLE_WALL_LENGTH * 14
    )

    field.try_place_unit(
        UnbreakableWall(LITTLE_WALL_LENGTH * 2, LITTLE_WALL_LENGTH),
        BIG_WALL_LENGTH * 12,
        LITTLE_WALL_LENGTH * 14
    )

    # асфальт
    field.try_place_unit(
        Asphalt(0, 0),
        LITTLE_WALL_LENGTH * 24,
        LITTLE_WALL_LENGTH * 14,
    )

    # враги
    spawner = TankBotSpawner(tank_to_go=3)
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(TankBot())

    field.spawners.append(spawner)
    field.try_place_unit(spawner, LITTLE_WALL_LENGTH * 24, 0)

    spawner = TankBotSpawner(tank_to_go=3)
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(TankBot())

    field.try_place_unit(spawner, LITTLE_WALL_LENGTH * 8,
                         LITTLE_WALL_LENGTH * 11)
    field.spawners.append(spawner)

    spawner = TankBotSpawner(tank_to_go=3)
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(ArmoredBot())

    field.try_place_unit(spawner, LITTLE_WALL_LENGTH * 12,
                         LITTLE_WALL_LENGTH * 18)
    field.spawners.append(spawner)

    bb = BonusBox()
    bb.next_bonuses = FireRapidBonus
    field.try_place_unit(
        bb,
        LITTLE_WALL_LENGTH * 12,
        LITTLE_WALL_LENGTH * 4,
    )

    field.units_for_step = field.units_for_step_buffer
    field.units_for_step_buffer = list()

    field.units_for_intersect = field.units_for_intersect_buffer
    field.units_for_intersect_buffer = list()

    return field
