from battle_city.game_logic_elements.game_constants import LITTLE_WALL_LENGTH, \
    PLAYER_TANK_HEALTH_POINTS, PLAYER_TANK_SPEED, PLAYER_TANK_COOL_DOWN, \
    BIG_WALL_LENGTH
from battle_city.game_logic_elements.game_field import GameField
from battle_city.game_logic_elements.units.armored_bot import ArmoredBot
from battle_city.game_logic_elements.units.asphalt import Asphalt
from battle_city.game_logic_elements.units.bonus_box import BonusBox
from battle_city.game_logic_elements.units.breakable_wall import BreakableWall
from battle_city.game_logic_elements.units.bush import Bush
from battle_city.game_logic_elements.units.heal_bot import HealBot
from battle_city.game_logic_elements.units.rapid_fire_bot import RapidFireBot
from battle_city.game_logic_elements.units.tank import Tank
from battle_city.game_logic_elements.units.tank_bot import TankBot
from battle_city.game_logic_elements.units.tank_bot_spawner import \
    TankBotSpawner
from battle_city.game_logic_elements.units.unbreakable_wall import \
    UnbreakableWall
from battle_city.game_logic_elements.upgrades.fire_rapid_bonus import \
    FireRapidBonus
from battle_city.game_logic_elements.upgrades.heal_bonus import HealBonus


def get_map() -> GameField:
    field = GameField()

    field.try_place_unit(
        Asphalt(LITTLE_WALL_LENGTH * 26, LITTLE_WALL_LENGTH * 26), 0, 0,
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH * 5, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH, BIG_WALL_LENGTH
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH * 5, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 7, BIG_WALL_LENGTH
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH * 11, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH, BIG_WALL_LENGTH * 3
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH * 4, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH, BIG_WALL_LENGTH * 6
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH * 4, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 8, BIG_WALL_LENGTH * 6
    )

    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH * 3, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 2, BIG_WALL_LENGTH * 10
    )

    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH * 3, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 8, BIG_WALL_LENGTH * 10
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH * 2),
        BIG_WALL_LENGTH, BIG_WALL_LENGTH * 7 + LITTLE_WALL_LENGTH
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH * 2),
        BIG_WALL_LENGTH * 11, BIG_WALL_LENGTH * 7 + LITTLE_WALL_LENGTH
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH),
        0, BIG_WALL_LENGTH * 12
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 3, BIG_WALL_LENGTH * 12
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 9, BIG_WALL_LENGTH * 12
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 12, BIG_WALL_LENGTH * 12
    )

    field.try_place_unit(
        BreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH * 3),
        BIG_WALL_LENGTH * 6, BIG_WALL_LENGTH * 5
    )

    #
    #
    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 5, BIG_WALL_LENGTH * 5 - LITTLE_WALL_LENGTH
    )

    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 7, BIG_WALL_LENGTH * 5 - LITTLE_WALL_LENGTH
    )

    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 5, BIG_WALL_LENGTH * 8 - LITTLE_WALL_LENGTH
    )

    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 7, BIG_WALL_LENGTH * 8 - LITTLE_WALL_LENGTH
    )

    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH, LITTLE_WALL_LENGTH),
        BIG_WALL_LENGTH * 12, BIG_WALL_LENGTH * 3
    )

    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH, LITTLE_WALL_LENGTH),
        0, BIG_WALL_LENGTH * 3
    )

    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH, LITTLE_WALL_LENGTH),
        BIG_WALL_LENGTH * 12, BIG_WALL_LENGTH * 8 - LITTLE_WALL_LENGTH
    )

    field.try_place_unit(
        UnbreakableWall(BIG_WALL_LENGTH, LITTLE_WALL_LENGTH),
        0, BIG_WALL_LENGTH * 8 - LITTLE_WALL_LENGTH
    )

    #
    #
    field.try_place_unit(
        Bush(BIG_WALL_LENGTH * 2, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 6 - LITTLE_WALL_LENGTH, 0
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH * 3, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 5, BIG_WALL_LENGTH * 2
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH * 3, BIG_WALL_LENGTH * 2),
        BIG_WALL_LENGTH, BIG_WALL_LENGTH * 4
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH * 3, BIG_WALL_LENGTH * 2),
        BIG_WALL_LENGTH * 9, BIG_WALL_LENGTH * 4
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH * 2, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 2, BIG_WALL_LENGTH * 8
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH * 2, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 9, BIG_WALL_LENGTH * 8
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH, BIG_WALL_LENGTH * 4 - LITTLE_WALL_LENGTH),
        BIG_WALL_LENGTH, BIG_WALL_LENGTH * 9 + LITTLE_WALL_LENGTH
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH, BIG_WALL_LENGTH * 4 - LITTLE_WALL_LENGTH),
        BIG_WALL_LENGTH * 11, BIG_WALL_LENGTH * 9 + LITTLE_WALL_LENGTH
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH, BIG_WALL_LENGTH * 2),
        BIG_WALL_LENGTH * 2, BIG_WALL_LENGTH * 11
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH, BIG_WALL_LENGTH * 2),
        BIG_WALL_LENGTH * 10, BIG_WALL_LENGTH * 11
    )

    field.try_place_unit(
        Bush(BIG_WALL_LENGTH * 3, BIG_WALL_LENGTH),
        BIG_WALL_LENGTH * 5, BIG_WALL_LENGTH * 10
    )

    #
    #
    spawner = TankBotSpawner(tank_to_go=5)
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    field.try_place_unit(spawner, 0, 0)
    field.spawners.append(spawner)

    spawner = TankBotSpawner(tank_to_go=5)
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(RapidFireBot())
    field.try_place_unit(spawner, BIG_WALL_LENGTH * 12, 0)
    field.spawners.append(spawner)

    spawner = TankBotSpawner(tank_to_go=5)
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(HealBot())
    field.try_place_unit(spawner, 0, BIG_WALL_LENGTH * 8)
    field.spawners.append(spawner)

    spawner = TankBotSpawner(tank_to_go=5)
    spawner.tanks_to_go.append(TankBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(ArmoredBot())
    spawner.tanks_to_go.append(RapidFireBot())
    field.try_place_unit(spawner, BIG_WALL_LENGTH * 12, BIG_WALL_LENGTH * 8)
    field.spawners.append(spawner)

    field.player = Tank()
    field.player.health_points = PLAYER_TANK_HEALTH_POINTS
    field.player.max_speed = PLAYER_TANK_SPEED
    field.player.shot_await_tick_count = PLAYER_TANK_COOL_DOWN
    field.try_place_unit(field.player, BIG_WALL_LENGTH * 6, BIG_WALL_LENGTH * 12)

    bb = BonusBox()
    bb.next_bonuses = HealBonus
    field.try_place_unit(
        bb,
        LITTLE_WALL_LENGTH * 12,
        LITTLE_WALL_LENGTH * 2,
    )

    bb = BonusBox()
    bb.next_bonuses = FireRapidBonus
    field.try_place_unit(
        bb,
        LITTLE_WALL_LENGTH * 12,
        LITTLE_WALL_LENGTH * 8,
    )

    field.units_for_step = field.units_for_step_buffer
    field.units_for_step_buffer = list()

    field.units_for_intersect = field.units_for_intersect_buffer
    field.units_for_intersect_buffer = list()

    return field
