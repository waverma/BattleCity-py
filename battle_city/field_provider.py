import os

from battle_city.game_logic_elements.game_constants \
    import LITTLE_WALL_LENGTH, \
    PLAYER_TANK_HEALTH_POINTS, PLAYER_TANK_SPEED, PLAYER_TANK_COOL_DOWN
from battle_city.game_logic_elements.game_field import GameField

from battle_city.game_logic_elements.units.bonus_box import BonusBox

import glob

from battle_city.game_logic_elements.units.tank import Tank
from battle_city.game_logic_elements.units.tank_bot_spawner import \
    TankBotSpawner

modules = [
    *glob.glob(
        os.path.join(
            os.path.normpath(
                os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir
            ),
            "battle_city", "game_logic_elements", "units", "*.py"
        )
    ),
    *glob.glob(
        os.path.join(
            os.path.normpath(
                os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir
            ),
            "battle_city", "game_logic_elements", "upgrades", "*.py"
        )
    )
]
for i in modules:
    exec("from " +
         '.'.join([
             i[:-3].split('\\')[-4],
             i[:-3].split('\\')[-3],
             i[:-3].split('\\')[-2],
             i[:-3].split('\\')[-1]
         ]) +
         " import *")


def load_from_file(full_file_name: str) -> GameField:
    with open(full_file_name, 'r', encoding='utf-8') as file:
        text_representation = file.read().split('\n')

    if (text_representation[0][:len("# MAP_FILE HEAD")] != "# MAP_FILE HEAD"
            and text_representation[-1] != "# MAP_FILE TAIL << AND"):
        return None

    field = GameField()
    field.width = int(
        text_representation[0].split(" << ")[1].split(" ")[0]
    ) * LITTLE_WALL_LENGTH
    field.height = int(
        text_representation[0].split(" << ")[1].split(" ")[1]
    ) * LITTLE_WALL_LENGTH

    collision = text_representation[0].split(" << ")[2].split(" ")
    field.player = Tank()
    field.player.health_points = PLAYER_TANK_HEALTH_POINTS
    field.player.max_speed = PLAYER_TANK_SPEED
    field.player.shot_await_tick_count = PLAYER_TANK_COOL_DOWN
    field.try_place_unit(
        field.player,
        LITTLE_WALL_LENGTH * int(collision[0]),
        LITTLE_WALL_LENGTH * int(collision[1])
    )

    for line in text_representation[1:-1]:
        if line[1] == "#":
            continue
        line_arguments = line.split(" << ")

        if line_arguments[0] == "ADD UNIT":
            collision = line_arguments[2].split(" ")
            unit = globals()[line_arguments[1]]()
            unit.collision.set_width(int(collision[2]) * LITTLE_WALL_LENGTH)
            unit.collision.set_height(int(collision[3]) * LITTLE_WALL_LENGTH)
            field.try_place_unit(
                    unit,
                    int(collision[0]) * LITTLE_WALL_LENGTH,
                    int(collision[1]) * LITTLE_WALL_LENGTH,
                    True
            )
        elif line_arguments[0] == "ADD SPAWNER":
            collision = line_arguments[1].split(" ")
            spawner = TankBotSpawner(tank_to_go=int(line_arguments[2]))
            for tank in line_arguments[3].split(" "):
                spawner.tanks_to_go.append(globals()[tank]())
            field.spawners.append(spawner)
            field.try_place_unit(
                spawner,
                int(collision[0]) * LITTLE_WALL_LENGTH,
                int(collision[1]) * LITTLE_WALL_LENGTH,
                True
            )
        elif line_arguments[0] == "ADD BONUS":
            collision = line_arguments[1].split(" ")
            bonus_box = BonusBox()
            bonus_box.next_bonuses = globals()[line_arguments[2]]
            field.try_place_unit(
                bonus_box,
                LITTLE_WALL_LENGTH * int(collision[0]),
                LITTLE_WALL_LENGTH * int(collision[1]),
                True
            )

    field.units_for_step = field.units_for_step_buffer
    field.units_for_step_buffer = list()

    field.units_for_intersect = field.units_for_intersect_buffer
    field.units_for_intersect_buffer = list()

    return field


def save_file(field: GameField, full_file_name: str):
    text_representation = [
        "# MAP_FILE HEAD << {} {} << {} {} {} {} << MAP 1".format(
            field.width // LITTLE_WALL_LENGTH,
            field.height // LITTLE_WALL_LENGTH,
            field.player.collision.x // LITTLE_WALL_LENGTH,
            field.player.collision.y // LITTLE_WALL_LENGTH,
            field.player.collision.w // LITTLE_WALL_LENGTH,
            field.player.collision.h // LITTLE_WALL_LENGTH
        )
    ]

    for unit in field.units:
        unit_type = type(unit)
        line = None
        if issubclass(unit_type, BonusBox):
            line = "ADD BONUS << {} {} {} {} << {}".format(
                unit.collision.x // LITTLE_WALL_LENGTH,
                unit.collision.y // LITTLE_WALL_LENGTH,
                unit.collision.w // LITTLE_WALL_LENGTH,
                unit.collision.h // LITTLE_WALL_LENGTH,
                unit.next_bonuses.__name__
            )
        elif issubclass(unit_type, TankBotSpawner):
            tanks = []
            for tank in unit.tanks_to_go:
                tanks.append(type(tank).__name__)
            line = "ADD SPAWNER << {} {} {} {} << {} << {}".format(
                unit.collision.x // LITTLE_WALL_LENGTH,
                unit.collision.y // LITTLE_WALL_LENGTH,
                unit.collision.w // LITTLE_WALL_LENGTH,
                unit.collision.h // LITTLE_WALL_LENGTH,
                unit.tank_to_go,
                " ".join(tanks)
            )
        else:
            if unit is not field.player:
                line = "ADD UNIT << {} << {} {} {} {}".format(
                    unit_type.__name__,
                    unit.collision.x // LITTLE_WALL_LENGTH,
                    unit.collision.y // LITTLE_WALL_LENGTH,
                    unit.collision.w // LITTLE_WALL_LENGTH,
                    unit.collision.h // LITTLE_WALL_LENGTH
                )

        if line is not None:
            text_representation.append(line)

    text_representation.append("# MAP_FILE TAIL << AND")

    with open(full_file_name, 'w', encoding='utf-8') as file:
        file.write('\n'.join(text_representation))


def get_all_maps():
    result = []
    maps_folder_path = os.path.join(
        os.path.normpath(
            os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir
        ),
        "resources", "maps"
    )

    os.chdir(maps_folder_path)
    for file in glob.glob("map_*"):
        if file[4:].isdecimal():
            result.append(load_from_file(os.path.join(maps_folder_path, file)))

    return result
