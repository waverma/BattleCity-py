from battle_city.buffers.buffer import Buffer
from battle_city.enums import Direction


class BufferToGameLogic(Buffer):
    def __init__(self):
        super().__init__()
        self.interface_stage = None

        self.is_cancel_button_pressed = False
        # MainMenu
        self.is_single_play_button_pressed = False
        self.is_network_button_pressed = False
        self.is_exit_button_pressed = False

        # Одиночная игра
        self.is_new_game_button_pressed = False

        # Сетевая игра
        self.is_new_session_create_button_pressed = False
        self.is_connect_button_pressed = False

        # Подключение
        self.connect_information = ""
        self.is_join_button_pressed = False

        # InGame
        self.user_prepare_direction = Direction.Up
        self.shot_request = False
        self.chat_open_key_pressed = False
        self.chat_close_key_pressed = False
        self.is_pause_request = False
        self.cheat_text = ''
        self.is_chat_open = False

        # Pause
        self.is_disconnect_button_pressed = False
        self.is_return_button_pressed = False

        # PostGame
        self.restart_request = False
        self.next_request = False
        self.is_to_main_menu_button_pressed = False
        self.game_info = ""

    def update(self, other: "BufferToGameLogic"):
        if other.is_locked or self.is_locked:
            return

        self.lock()
        other.lock()

        self.is_cancel_button_pressed = other.is_cancel_button_pressed
        # MainMenu
        self.is_single_play_button_pressed = (
            other.is_single_play_button_pressed
        )
        self.is_network_button_pressed = other.is_network_button_pressed
        self.is_exit_button_pressed = other.is_exit_button_pressed

        # Одиночная игра
        self.is_new_game_button_pressed = other.is_new_game_button_pressed

        # Сетевая игра
        self.is_new_session_create_button_pressed = (
            other.is_new_session_create_button_pressed
        )
        self.is_connect_button_pressed = other.is_connect_button_pressed

        # Подключение
        self.connect_information = other.connect_information
        self.is_join_button_pressed = other.is_join_button_pressed

        # InGame
        self.user_prepare_direction = other.user_prepare_direction
        self.shot_request = other.shot_request
        self.chat_open_key_pressed = other.chat_open_key_pressed
        self.chat_close_key_pressed = other.chat_close_key_pressed
        self.is_pause_request = other.is_pause_request
        self.cheat_text = other.cheat_text  # НЕ ПОТОКОБЕЗОПАСНО!!!
        self.is_chat_open = other.is_chat_open

        # Pause
        self.is_disconnect_button_pressed = other.is_disconnect_button_pressed
        self.is_return_button_pressed = other.is_return_button_pressed

        # PostGame
        self.restart_request = other.restart_request
        self.next_request = other.next_request
        self.is_to_main_menu_button_pressed = (
            other.is_to_main_menu_button_pressed
        )
        self.game_info = other.game_info

        other.unlock()
        self.unlock()

    def copy(self):
        while self.is_locked:
            pass

        other = BufferToGameLogic()
        self.lock()

        other.is_cancel_button_pressed = self.is_cancel_button_pressed
        # MainMenu
        other.is_single_play_button_pressed = (
            self.is_single_play_button_pressed
        )
        other.is_network_button_pressed = self.is_network_button_pressed
        other.is_exit_button_pressed = self.is_exit_button_pressed

        # Одиночная игра
        other.is_new_game_button_pressed = self.is_new_game_button_pressed

        # Сетевая игра
        other.is_new_session_create_button_pressed = (
            self.is_new_session_create_button_pressed
        )
        other.is_connect_button_pressed = self.is_connect_button_pressed

        # Подключение
        other.connect_information = self.connect_information
        other.is_join_button_pressed = self.is_join_button_pressed

        # InGame
        other.user_prepare_direction = self.user_prepare_direction
        other.shot_request = self.shot_request
        other.chat_open_key_pressed = self.chat_open_key_pressed
        other.chat_close_key_pressed = self.chat_close_key_pressed
        other.is_pause_request = self.is_pause_request
        other.is_chat_open = self.is_chat_open
        other.cheat_text = self.cheat_text  # НЕ ПОТОКОБЕЗОПАСНО!!!

        # Pause
        other.is_disconnect_button_pressed = self.is_disconnect_button_pressed
        other.is_return_button_pressed = self.is_return_button_pressed

        # PostGame
        other.restart_request = self.restart_request
        other.next_request = self.next_request
        other.is_to_main_menu_button_pressed = (
            self.is_to_main_menu_button_pressed
        )
        other.game_info = self.game_info

        self.unlock()

        return other

    def __iter__(self):
        pass

    def __next__(self):
        pass
