from pygame.rect import Rect

from graphic_elements.draw_information import DrawInformation
from enums.direction import Direction
from enums.tank_texture_kind import TankTextureKind
from game_logic_elements.units.bullet import Bullet
from game_logic_elements.units.unit import Unit


class Tank(Unit):
    texture_name = "Tanks.png"

    def __init__(self, tank_color=TankTextureKind.GreenThree):
        super().__init__()
        self.collision = Rect(-1, -1, 34, 34)
        self.max_speed = 3
        self.current_direction = Direction.Up
        self.location_to_bullet = None
        self.color = (0, 0, 255)

        self.shot_await_tick_count = 50
        self.shot_await_tick_pointer = 0

        self.tank_image_rect = Tank.get_tank_image_rect(tank_color, 0)

    def step(self, field):
        super().step(field)
        if self.velocity[0] > 0:
            self.current_direction = Direction.Right
        if self.velocity[0] < 0:
            self.current_direction = Direction.Left
        if self.velocity[1] > 0:
            self.current_direction = Direction.Down
        if self.velocity[1] < 0:
            self.current_direction = Direction.Up

        if self.shot_await_tick_pointer > 0:
            self.shot_await_tick_pointer += 1
        if self.shot_await_tick_pointer == self.shot_await_tick_count:
            self.shot_await_tick_pointer = 0

    def on_shot(self, field, rect: Rect):
        if self.health_points == 0:
            field.try_remove_unit(self)
        else:
            self.health_points -= 1

    def shot(self, field):
        bullet_spawn_padding = 1
        if self.shot_await_tick_pointer > 0:
            return
        self.shot_await_tick_pointer = 1
        bullet = Bullet(self)
        bullet.current_direction = self.current_direction
        bullet.set_velocity(bullet.current_direction)
        if self.current_direction == Direction.Right:
            self.location_to_bullet = (
                self.collision.x + self.collision.width + bullet_spawn_padding + self.max_speed,
                self.collision.y + self.collision.height / 2 - bullet.collision.height / 2
            )
        if self.current_direction == Direction.Left:
            self.location_to_bullet = (
                self.collision.x - bullet.collision.width - bullet_spawn_padding - self.max_speed,
                self.collision.y + self.collision.height / 2 - bullet.collision.height / 2
            )
        if self.current_direction == Direction.Up:
            self.location_to_bullet = (
                self.collision.x + self.collision.width / 2 - bullet.collision.width / 2,
                self.collision.y - bullet.collision.height - bullet_spawn_padding - self.max_speed
            )
        if self.current_direction == Direction.Down:
            self.location_to_bullet = (
                self.collision.x + self.collision.width / 2 - bullet.collision.width / 2,
                self.collision.y + self.collision.height + bullet_spawn_padding + self.max_speed
            )

        if not field.try_place_unit(bullet, self.location_to_bullet[0], self.location_to_bullet[1]):
            explosion_rect = Rect(self.location_to_bullet[0], self.location_to_bullet[1],
                                  bullet.collision.width, bullet.collision.height)
            units = field.get_intersected_units(explosion_rect)
            if len(units) == 0:
                self.shot_await_tick_pointer = 0
            for unit in units:
                unit.on_shot(field, explosion_rect)

    def get_draw_info(self) -> list:
        result = list()

        result.append(DrawInformation(
            texture_name=Tank.texture_name,
            draw_rect=self.collision,
            texture_rect=[  # TODO Перенести в константы графики
                self.tank_image_rect[self.current_direction][0] * 1.9+5,
                self.tank_image_rect[self.current_direction][1] * 1.9+5,
                self.tank_image_rect[self.current_direction][2] * 1.9,
                self.tank_image_rect[self.current_direction][3] * 1.9
            ]
        ))

        return result

    @staticmethod
    def get_tank_image_rect(tank_color: TankTextureKind, kind: int) -> tuple:
        tank_block = (32 * 4, 32)  # TODO Перенести в константы графики
        tank = (32, 32)

        return (
            [tank_color * tank_block[0], tank_block[1] * kind, tank[0], tank[1]],
            [tank_color * tank_block[0] + tank[0] * 1, tank_block[1] * kind, tank[0], tank[1]],
            [tank_color * tank_block[0] + tank[0] * 2, tank_block[1] * kind, tank[0], tank[1]],
            [tank_color * tank_block[0] + tank[0] * 3, tank_block[1] * kind, tank[0], tank[1]]
        )
