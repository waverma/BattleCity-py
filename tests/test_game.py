from unittest import TestCase

from battle_city.buffers.buffer_to_game_logic import BufferToGameLogic
from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.enums import InterfaceStage
from battle_city.game_logic_elements.game import Game
from battle_city.game_logic_elements.game_constants import (
    BIG_FIRE_RATE,
    BIG_SPEED,
    GOD_MOD,
    HEAL_CHEAT,
)


class TestGame(TestCase):
    def test_extract_to_render(self):
        game = Game()
        game.try_set_new_field()
        render_info = game.extract_to_render(BufferToRender())

        self.assertEqual(render_info.player[0][0], game.field.player.type)
        self.assertEqual(render_info.player[0][1], game.field.player.collision)
        self.assertEqual(
            render_info.player[0][2], game.field.player.current_direction
        )
        self.assertEqual(
            render_info.health_points, game.field.player.health_points
        )
        self.assertEqual(len(render_info.units) + 1, len(game.field.units))

    def test_set_cheat(self):
        game = Game()
        game.try_set_new_field()

        line = "djkgf{}".format(HEAL_CHEAT)
        game.set_cheat(line)
        self.assertTrue(game.is_cheat_used)
        game.set_cheat(line)
        self.assertTrue(game.is_cheat_used)
        game.set_cheat("{}d".format(line))
        self.assertFalse(game.is_cheat_used)

        line = "djkgf{}".format(BIG_SPEED)
        game.set_cheat(line)
        self.assertTrue(game.is_cheat_used)
        game.set_cheat(line)
        self.assertTrue(game.is_cheat_used)
        game.set_cheat("{}d".format(line))
        self.assertFalse(game.is_cheat_used)

        line = "djkgf{}".format(GOD_MOD)
        game.set_cheat(line)
        self.assertTrue(game.is_cheat_used)
        game.set_cheat(line)
        self.assertTrue(game.is_cheat_used)
        game.set_cheat("{}d".format(line))
        self.assertFalse(game.is_cheat_used)

        line = "djkgf{}".format(BIG_FIRE_RATE)
        game.set_cheat(line)
        self.assertTrue(game.is_cheat_used)
        game.set_cheat(line)
        self.assertTrue(game.is_cheat_used)
        game.set_cheat("{}d".format(line))
        self.assertFalse(game.is_cheat_used)

    def test_update(self):
        game = Game()
        game.try_set_new_field()

        buffer = BufferToGameLogic()
        game.stage = buffer.interface_stage = InterfaceStage.InGame

        game.update(buffer, BufferToRender())
        self.assertEqual(game.stage, InterfaceStage.InGame)

    def test_is_game_completed(self):
        game = Game()
        game.try_set_new_field()
        for spawner in game.field.spawners:
            spawner.tank_to_go = 0
        game.field.spawners[0].tank_to_go = 1

        self.assertFalse(game.is_game_completed()[0])

        game.field.spawners[0].tank_to_go = 0

        self.assertFalse(game.is_game_completed()[0])
        self.assertTrue(game.is_game_completed()[1])

        game.field.spawners[0].tank_to_go = 1
        game.field.update()

        self.assertFalse(game.is_game_completed()[0])
        self.assertTrue(game.is_game_completed()[1])
