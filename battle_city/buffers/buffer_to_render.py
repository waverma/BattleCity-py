from battle_city.buffers.buffer import Buffer
from battle_city.enums.interface_stage import InterfaceStage


class BufferToRender(Buffer):
    def __init__(self):
        super().__init__()
        self.game_stage = InterfaceStage.MainMenu

        self.units = list()
        self.player = None
        self.points = ""
        self.cool_dawn = ""
        self.health_points = (0, 0, 0, 0, 0)
        self.speed = ""
        self.battle_result = ""
        self.field_size = (0, 0)
        self.chat_text = list()
        self.is_chat_on = False

    def update(self, other: "BufferToRender"):
        if other.is_locked or self.is_locked:
            return

        self.lock()
        other.lock()

        self.units = other.units  # НЕ ПОТОКОБЕЗОПАСНО!!!
        self.points = other.points
        self.cool_dawn = other.cool_dawn
        self.health_points = other.health_points
        self.game_stage = other.game_stage
        self.field_size = other.field_size
        self.player = other.player
        self.chat_text = other.chat_text  # НЕ ПОТОКОБЕЗОПАСНО!!!
        self.is_chat_on = other.is_chat_on
        self.battle_result = other.battle_result
        self.speed = other.speed

        other.unlock()
        self.unlock()

    def copy(self):
        while self.is_locked:
            pass

        other = BufferToRender()
        self.lock()

        other.units = self.units  # НЕ ПОТОКОБЕЗОПАСНО!!!
        other.points = self.points
        other.cool_dawn = self.cool_dawn
        other.health_points = self.health_points
        other.game_stage = self.game_stage
        other.field_size = self.field_size
        other.player = self.player
        other.chat_text = self.chat_text  # НЕ ПОТОКОБЕЗОПАСНО!!!
        other.is_chat_on = self.is_chat_on
        other.battle_result = self.battle_result
        other.speed = self.speed

        self.unlock()

        return other

    def __iter__(self):
        pass

    def __next__(self):
        pass
