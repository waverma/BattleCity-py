import copy

from buffers.buffer import Buffer


class UserEvent(Buffer):
    def __init__(self):
        super().__init__()
        self.absolute_mouse_location = (0, 0)
        self.is_right_mouse_click = False
        self.is_left_mouse_click = False
        self.was_right_mouse_click = False
        self.was_left_mouse_click = False
        self.focus_element = None
        self.events = None

        self.pressed_buttons = list()
        self.non_released_buttons = list()

    def update(self, other: 'UserEvent'):
        if other.is_locked or self.is_locked:
            return

        self.lock()
        other.lock()

        self.absolute_mouse_location = other.absolute_mouse_location
        self.is_right_mouse_click = other.is_right_mouse_click
        self.is_left_mouse_click = other.is_left_mouse_click
        self.was_right_mouse_click = other.was_right_mouse_click
        self.was_left_mouse_click = other.was_left_mouse_click
        self.focus_element = other.focus_element

        self.pressed_buttons = copy.deepcopy(other.pressed_buttons)
        self.non_released_buttons = copy.deepcopy(other.non_released_buttons)

        self.events = other.events

        self.unlock()
        other.unlock()

    def copy(self):
        while self.is_locked:
            pass
        other = UserEvent()
        self.lock()

        other.absolute_mouse_location = self.absolute_mouse_location
        other.is_right_mouse_click = self.is_right_mouse_click
        other.is_left_mouse_click = self.is_left_mouse_click
        other.was_right_mouse_click = self.was_right_mouse_click
        other.was_left_mouse_click = self.was_left_mouse_click
        other.focus_element = self.focus_element
        other.events = self.events

        other.pressed_buttons = copy.deepcopy(self.pressed_buttons)
        other.non_released_buttons = copy.deepcopy(self.non_released_buttons)

        self.unlock()
        return other
