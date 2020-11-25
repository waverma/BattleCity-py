import copy

import pygame
from battle_city.buffers.buffer_to_game_logic import BufferToGameLogic
from battle_city.buffers.buffer_to_render import BufferToRender
from battle_city.buffers.drawing_buffer import DrawingBuffer
from battle_city.buffers.user_event import UserEvent
from battle_city.enums.interface_stage import InterfaceStage
from battle_city.game_logic_elements.game import Game
from battle_city.graphic_elements.graphic_utils import GraphicUtils
from battle_city.graphic_elements.gui_elements.user_interface import UserInterface
from battle_city.graphic_elements.texture_provider import TextureProvider


class GameLoop:
    def __init__(self, width, height):
        # настройка PyGame
        pygame.init()
        self.display = pygame.display.set_mode((width, height))
        self.is_window_closed = False
        pygame.display.set_caption("Battle City")

        self.buffer_to_draw = DrawingBuffer()
        self.buffer_to_render = BufferToRender()
        self.buffer_to_game_logic = BufferToGameLogic()
        self.buffer_to_game_logic.interface_stage = InterfaceStage.MainMenu
        self.events = UserEvent()
        self.game = Game()
        self.user_interface = UserInterface()
        self.mouse_pos = (0, 0)

    def run(self):
        while not self.is_window_closed:
            pygame.time.delay(20)
            self.display.fill(GraphicUtils.DEFAULT_DISPLAY_COLOR)

            self.get_event(self.events)
            self.user_interface.update(
                self.events, self.game.stage, self.buffer_to_game_logic
            )
            self.game.update(self.buffer_to_game_logic, self.buffer_to_render)
            self.user_interface.render(
                self.buffer_to_render, self.buffer_to_draw
            )
            self.draw(self.buffer_to_draw)

            if self.buffer_to_game_logic.is_exit_button_pressed:
                quit()

            pygame.display.update()

    def get_event(self, events):
        user_event = events
        if user_event.pressed_buttons is None:
            user_event.pressed_buttons = [0 for _ in range(513)]
        user_event.was_left_mouse_click = user_event.is_left_mouse_click
        user_event.was_right_mouse_click = user_event.is_right_mouse_click
        user_event.non_released_buttons = copy.deepcopy(
            user_event.pressed_buttons
        )
        user_event.events = pygame.event.get()
        for e in user_event.events:
            if e.type == pygame.QUIT:
                self.is_window_closed = True

            if e.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                user_event.pressed_buttons = copy.deepcopy(keys)

            if e.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()
                user_event.pressed_buttons = copy.deepcopy(keys)

            if e.type == pygame.MOUSEMOTION:
                self.mouse_pos = e.pos

            if e.type == pygame.MOUSEBUTTONDOWN:
                user_event.is_left_mouse_click = e.button == 1
                user_event.is_right_mouse_click = e.button == 3

            if e.type == pygame.MOUSEBUTTONUP:
                user_event.is_left_mouse_click = e.button != 1
                user_event.is_right_mouse_click = e.button != 3

        user_event.absolute_mouse_location = self.mouse_pos

        self.events = user_event

    def draw(self, buffer: DrawingBuffer):
        for draw_element in buffer:
            (
                transform,
                texture_name,
                rect,
                texture_rect,
                texture_rotate,
                fillcolor,
                outline_color,
                outline_size,
                text,
                text_color,
                text_size,
                image_transform,
            ) = draw_element.get_to_unpack()

            x = rect.x * transform[2] + transform[0]
            y = rect.y * transform[3] + transform[1]
            width = rect.width * transform[2]
            height = rect.height * transform[3]

            if outline_size is not None and outline_color is not None:
                outline_rect = [
                    x - outline_size,
                    y - outline_size,
                    width + outline_size * 2,
                    height + outline_size * 2,
                ]
                pygame.draw.rect(self.display, outline_color, outline_rect)

            if fillcolor is not None:
                pygame.draw.rect(
                    self.display, fillcolor, [x, y, width, height]
                )

            if texture_name is not None:
                texture, texture_rect = TextureProvider.textures[
                    texture_name[0]
                ].get_texture(texture_name[1], image_transform)
                if texture_rotate is not None:
                    texture = pygame.transform.rotate(texture, texture_rotate)
                if texture_rect is not None:
                    self.display.blit(texture, (x, y), texture_rect)
                else:
                    self.display.blit(texture, (x, y))
            if text is not None:
                self.display.blit(
                    pygame.font.SysFont("arial", text_size).render(
                        text, True, text_color
                    ),
                    (x, y),
                )
