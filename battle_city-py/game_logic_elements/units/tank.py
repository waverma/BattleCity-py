from pygame.rect import Rect

from enums.unit_type import UnitType
from enums.direction import Direction
from game_logic_elements.units.bullet import Bullet
from game_logic_elements.units.unit import Unit


class Tank(Unit):
    def __init__(self):
        super().__init__()
        self.collision = Rect(-1, -1, 32, 32)
        self.max_speed = 2
        self.current_direction = Direction.Up
        self.type = UnitType.TankRed
        self.location_to_bullet = None

        self.shot_await_tick_count = 50
        self.shot_await_tick_pointer = 0

    def step(self, field: 'GameField'):
        super().step(field)

        if self.shot_await_tick_pointer > 0:
            self.shot_await_tick_pointer += 1
        if self.shot_await_tick_pointer == self.shot_await_tick_count:
            self.shot_await_tick_pointer = 0

    def on_shot(self, field: 'GameField', rect: Rect):
        if self.health_points == 0:
            field.try_remove_unit(self)
        else:
            self.health_points -= 1

    def shot(self, field: 'GameField'):
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
