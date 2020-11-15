from pygame.rect import Rect

from enums.direction import Direction


class Unit:
    def __init__(self):
        self.collision = Rect(-1, -1, -1, -1)
        self.max_speed = 0
        self.health_points = 1
        self.color = (0, 0, 0)

        self.velocity = (0, 0)
        self.actions = list()

    def set_velocity(self, direction: Direction):
        if direction == Direction.Up:
            self.velocity = (0, -self.max_speed)
        if direction == Direction.Right:
            self.velocity = (self.max_speed, 0)
        if direction == Direction.Down:
            self.velocity = (0, self.max_speed)
        if direction == Direction.Left:
            self.velocity = (-self.max_speed, 0)
        if direction == Direction.Null:
            self.velocity = (0, 0)

    def on_shot(self, field, rect: Rect):
        if self.health_points == 0:
            self.on_explosion(field, rect)
        else:
            self.health_points -= 1

    def step(self, field):
        if self.velocity[0] != 0 or self.velocity[1] != 0:
            self.move_step(field)

        for action in self.actions:
            action()
        self.actions = list()

    def move_step(self, field):
        x_saved = self.collision.left
        y_saved = self.collision.top

        field.try_remove_unit(self)
        if not field.try_place_unit(self, x_saved + self.velocity[0], y_saved + self.velocity[1]):
            field.try_place_unit(self, x_saved, y_saved)

    def on_explosion(self, field, explosion_rect: Rect):
        pass

    def is_intersected_with_unit(self, other: 'Unit') -> bool:
        return self.collision.colliderect(other.collision)

    def is_intersected_with_rect(self, rect: Rect) -> bool:
        return self.collision.colliderect(rect)

    def get_draw_info(self) -> list:
        return list()
        # (
        # texture_name,
        # rect,
        # texture_rect,
        # texture_rotate,
        # fill_color,
        # outline_color,
        # outline_size,
        # text,
        # text_color,
        # text_size
        # )
