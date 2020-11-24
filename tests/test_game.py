from unittest import TestCase
from battle_city.game_logic_elements.game import Game


class TestGame(TestCase):
    def test_extract_to_render(self):
        game = Game()
        game.set_new_field()
        render_info = game.extract_to_render()

        self.assertEqual(render_info.player[0][0], game.field.player.type)
        self.assertEqual(render_info.player[0][1], game.field.player.collision)
        self.assertEqual(
            render_info.player[0][2], game.field.player.current_direction
        )
        self.assertEqual(
            render_info.health_points, game.field.player.health_points
        )
        self.assertEqual(len(render_info.units) + 1, len(game.field.units))

    def test_is_game_completed(self):
        game = Game()
        game.set_new_field()
        for spawner in game.field.spawners:
            spawner.tank_to_go = 0
        game.field.spawners[0].tank_to_go = 1

        self.assertFalse(game.is_game_completed()[0])

        game.field.spawners[0].tank_to_go = 0

        self.assertTrue(game.is_game_completed()[0])
        self.assertTrue(game.is_game_completed()[1])

        game.field.spawners[0].tank_to_go = 1
        game.field.try_remove_unit(game.field.player)
        game.field.update()

        self.assertTrue(game.is_game_completed()[0])
        self.assertFalse(game.is_game_completed()[1])
