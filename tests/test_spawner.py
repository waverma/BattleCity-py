from unittest import TestCase
from battle_city.game_logic_elements.game_field import GameField
from battle_city.game_logic_elements.units.tank_bot_spawner import TankBotSpawner
from battle_city.rect import Rect


class TestTankBotSpawner(TestCase):
    def test_step(self):
        field = GameField()
        field_rectangle = Rect(0, 0, field.width, field.height)
        spawner = TankBotSpawner()
        field.try_place_unit(spawner, 1, 1)
        spawner.no_tank_tick_pointer = spawner.no_tank_tick_count

        spawner.step(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 1)

        spawner.step(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 1)

        spawner.no_tank_tick_pointer = spawner.no_tank_tick_count
        spawner.step(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 1)

        spawner.no_tank_tick_pointer = 0
        field.try_remove_unit(spawner.current_tank)
        field.update()
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 0)

        spawner.no_tank_tick_pointer = spawner.no_tank_tick_count
        spawner.is_tank_alive = False
        spawner.step(field)
        spawner.no_tank_tick_pointer = spawner.no_tank_tick_count
        spawner.current_tank.collision = Rect(70, 70, 32, 32)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 1)

        spawner.step(field)
        self.assertEqual(len(field.get_intersected_units(field_rectangle)), 1)
