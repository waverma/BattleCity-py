from battle_city.buffers.buffer_to_game_logic import BufferToGameLogic
from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.enums.interface_stage import InterfaceStage
from battle_city.game_logic_elements.game_field import GameField


class Game:
    def __init__(self):
        self.field = None
        self.set_new_field()
        self.stage = InterfaceStage.MainMenu
        self.score = 0

        self.god_mode = True

    def is_game_completed(self):
        battle_result = True
        for spawner in self.field.spawners:
            battle_result = (
                battle_result
                and spawner.tank_to_go == 0
                and not spawner.is_tank_alive
            )
        return (
            not self.god_mode and (self.field.player not in self.field.units or battle_result),
            self.field.player in self.field.units,
        )

    def update(self, buffer: BufferToGameLogic, output_buffer: BufferToRender):

        if buffer.interface_stage == InterfaceStage.InGame:
            self.user_impact(buffer)
            self.field.update()
            if self.is_game_completed()[0]:
                self.stage = InterfaceStage.PostGame
            if buffer.is_pause_request:
                self.stage = InterfaceStage.Pause

        if buffer.interface_stage == InterfaceStage.MainMenu:
            if buffer.is_single_play_button_pressed:
                self.stage = InterfaceStage.SinglePlayMenu

        if buffer.interface_stage == InterfaceStage.SinglePlayMenu:
            if buffer.is_cancel_button_pressed:
                self.stage = InterfaceStage.MainMenu
            if buffer.is_new_game_button_pressed:
                self.set_new_field()
                self.stage = InterfaceStage.InGame

        if buffer.interface_stage == InterfaceStage.PostGame:
            if buffer.restart_request:
                self.set_new_field()
                self.stage = InterfaceStage.InGame
            if buffer.is_to_main_menu_button_pressed:
                self.stage = InterfaceStage.MainMenu

        if buffer.interface_stage == InterfaceStage.Pause:
            if buffer.is_to_main_menu_button_pressed:
                self.stage = InterfaceStage.MainMenu
            if buffer.is_return_button_pressed:
                self.stage = InterfaceStage.InGame

        output_buffer.update(self.extract_to_render())

    def user_impact(self, buffer: BufferToGameLogic):
        self.field.player.set_velocity(buffer.user_prepare_direction)
        if buffer.shot_request:
            self.field.player.actions.append(
                lambda: self.field.player.shot(self.field)
            )

    def extract_to_render(self) -> BufferToRender:
        buffer = BufferToRender()
        buffer.field_size = self.field.width, self.field.height
        buffer.points = str(self.score)
        if self.is_game_completed()[1]:
            buffer.battle_result = "Победа"
        else:
            buffer.battle_result = "Поражение"
        buffer.health_points = self.field.player.health_points
        buffer.cool_dawn = "{0} / {1}".format(
            str((self.field.player.shot_await_tick_count * 20) / 1000),
            str(
                ((self.field.player.shot_await_tick_count * 20) / 1000)
                - ((self.field.player.shot_await_tick_pointer * 20) / 1000)
            )[0:4],
        )
        buffer.game_stage = self.stage

        a = list()
        b = list()
        c = list()

        for unit in self.field.units:
            if unit is not self.field.player:
                # if unit is Tank
                buffer.units.append(unit.get_render_info())
            else:
                buffer.player = unit.get_render_info()

        return buffer

    def set_new_field(self):
        self.field = GameField()
        self.field.set_test_game_field()
        self.field.game = self
