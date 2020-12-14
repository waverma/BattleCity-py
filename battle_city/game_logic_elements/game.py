from typing import Tuple

from battle_city.buffers.buffer_to_game_logic import BufferToGameLogic
from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.enums import InterfaceStage, UnitType
from battle_city.field_provider import get_all_maps
from battle_city.game_logic_elements.game_constants import (
    BIG_FIRE_RATE,
    BIG_SPEED,
    COOL_DOWN_VALUE,
    GOD_COOL_DOWN,
    GOD_HP,
    GOD_MOD,
    GOD_SPEED,
    HEAL_CHEAT,
    HEAL_VALUE,
    SPEED_VALUE,
)


def get_cool_down(tick_count, tick_pointer) -> Tuple:
    return (
        str((tick_count * 20) / 1000),
        str(
            round(((tick_count * 20) / 1000) - ((tick_pointer * 20) / 1000), 4)
        ),
    )


class Game:
    def __init__(self):
        self.field = None
        self.stage = InterfaceStage.MainMenu

        self.kills = 0
        self.tank_bot_kills = 0
        self.heal_bot_kills = 0
        self.armored_bot_kills = 0
        self.rapid_fire_kills = 0

        self.is_cheat_used = False

        self.maps = list()
        self.current_map = 1

        self.god_mode = False
        self.set_maps()

    def is_game_completed(self):
        battle_result = True
        for spawner in self.field.spawners:
            battle_result = (
                battle_result and spawner.type == UnitType.EmptyBotSpawner
            )
        return (
            not self.god_mode
            and (self.field.player not in self.field.units or battle_result),
            self.field.player in self.field.units,
        )

    def update(self, buffer: BufferToGameLogic, output_buffer: BufferToRender):

        if buffer.interface_stage == InterfaceStage.InGame:
            self.user_impact(buffer)
            self.field.update()
            if self.is_game_completed()[0]:
                if (
                    self.is_game_completed()[1]
                    and len(self.maps) > self.current_map
                ):
                    self.stage = InterfaceStage.PostGameAfterWin
                else:
                    self.stage = InterfaceStage.PostGame
            elif buffer.is_pause_request:
                self.stage = InterfaceStage.Pause

        if buffer.interface_stage == InterfaceStage.MainMenu:
            if buffer.is_single_play_button_pressed:
                self.stage = InterfaceStage.SinglePlayMenu

        if buffer.interface_stage == InterfaceStage.SinglePlayMenu:
            if buffer.is_cancel_button_pressed:
                self.stage = InterfaceStage.MainMenu
            if buffer.is_new_game_button_pressed:
                self.try_set_new_field()
                self.stage = InterfaceStage.InGame

        if buffer.interface_stage == InterfaceStage.PostGame:
            if buffer.restart_request:
                self.set_maps()
                self.try_set_new_field()
                self.stage = InterfaceStage.InGame
            if buffer.is_to_main_menu_button_pressed:
                self.stage = InterfaceStage.MainMenu

        if buffer.interface_stage == InterfaceStage.PostGameAfterWin:
            if buffer.next_request:
                self.try_set_new_field()
                self.stage = InterfaceStage.InGame
            if buffer.is_to_main_menu_button_pressed:
                self.stage = InterfaceStage.MainMenu

        if buffer.interface_stage == InterfaceStage.Pause:
            if buffer.is_to_main_menu_button_pressed:
                self.stage = InterfaceStage.MainMenu
            if buffer.is_return_button_pressed:
                self.stage = InterfaceStage.InGame

        self.extract_to_render(output_buffer)

    def user_impact(self, buffer: BufferToGameLogic):
        self.set_cheat(buffer.cheat_text)
        self.field.player.set_velocity(buffer.user_prepare_direction)
        if buffer.shot_request:
            self.field.player.actions.append(
                lambda: self.field.player.shot(self.field)
            )

    def extract_to_render(self, output_buffer) -> BufferToRender:
        buffer = output_buffer
        buffer.points = (
            self.kills,
            self.tank_bot_kills,
            self.armored_bot_kills,
            self.heal_bot_kills,
            self.rapid_fire_kills,
        )

        if self.field is not None:
            buffer.field_size = self.field.width, self.field.height
            buffer.speed = str(
                abs(self.field.player.velocity[0])
                + abs(self.field.player.velocity[1])
            )
            buffer.battle_result = (
                self.is_game_completed()[0],
                self.is_game_completed()[1],
            )
            buffer.health_points = self.field.player.health_points

            buffer.cool_dawn = get_cool_down(
                self.field.player.shot_await_tick_count,
                self.field.player.shot_await_tick_pointer,
            )

            if self.field.player.current_bonus is not None:
                buffer.bonus_cool_dawn = (
                    *get_cool_down(
                        self.field.player.current_bonus.action_duration,
                        self.field.player.current_bonus.tick_pointer,
                    ),
                    self.field.player.current_bonus.type,
                )
            else:
                buffer.bonus_cool_dawn = (0, 0, None)

            for unit in self.field.units:
                if unit is not self.field.player:
                    buffer.units.append(unit.get_render_info())
                else:
                    buffer.player = unit.get_render_info()

        buffer.game_stage = self.stage

        return buffer

    def set_cheat(self, cheat_line: str):
        if not self.is_cheat_used:
            if cheat_line[-len(HEAL_CHEAT):] == HEAL_CHEAT:
                self.field.player.health_points += HEAL_VALUE
                self.is_cheat_used = True
            elif cheat_line[-len(BIG_SPEED):] == BIG_SPEED:
                self.field.player.max_speed = SPEED_VALUE
                self.is_cheat_used = True
            elif cheat_line[-len(GOD_MOD):] == GOD_MOD:
                self.field.player.health_points = GOD_HP
                self.field.player.max_speed = GOD_SPEED
                self.field.player.shot_await_tick_count = GOD_COOL_DOWN
                self.is_cheat_used = True
            elif cheat_line[-len(BIG_FIRE_RATE):] == BIG_FIRE_RATE:
                self.field.player.shot_await_tick_count = COOL_DOWN_VALUE
                self.is_cheat_used = True

        if (
            cheat_line[-len(HEAL_CHEAT):] != HEAL_CHEAT
            and cheat_line[-len(BIG_SPEED):] != BIG_SPEED
            and cheat_line[-len(GOD_MOD):] != GOD_MOD
            and cheat_line[-len(BIG_FIRE_RATE):] != BIG_FIRE_RATE
        ):
            self.is_cheat_used = False

    def set_maps(self):
        self.maps = list()
        self.current_map = 0
        self.maps = get_all_maps()

    def try_set_new_field(self) -> bool:
        if self.current_map >= len(self.maps):
            return False

        self.field = self.maps[self.current_map]
        self.current_map += 1
        self.kills = 0
        self.field.game = self

        return True
