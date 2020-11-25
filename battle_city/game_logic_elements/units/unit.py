from battle_city.enums.direction import Direction
from battle_city.enums.unit_type import UnitType
from battle_city.rect import Rect


class Unit:
    def __init__(self):
        self.collision = Rect(-1, -1, -1, -1)
        self.max_speed = 0
        self.health_points = 1
        self.current_direction = Direction.Up
        self.velocity = (0, 0)
        self.actions = list()

        self.type = UnitType.Null

    def set_velocity(self, direction: Direction):
        if direction != Direction.Null:
            self.current_direction = direction
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
        self.health_points -= 1
        if self.health_points <= 0:
            self.on_explosion(field, rect)

    def step(self, field):
        if self.velocity[0] != 0 or self.velocity[1] != 0:
            self.move_step(field)

        for action in self.actions:
            action()
        self.actions = list()

    def move_step(self, field):
        x_saved = self.collision.x
        y_saved = self.collision.y

        field.try_remove_unit(self)
        if not field.try_place_unit(
            self, x_saved + self.velocity[0], y_saved + self.velocity[1]
        ):
            field.try_place_unit(self, x_saved, y_saved)

    def on_explosion(self, field, explosion_rect: Rect):
        pass

    def is_intersected_with_unit(self, other: "Unit") -> bool:
        return self.is_intersected_with_rect(other.collision)

    def is_intersected_with_rect(self, rect: Rect) -> bool:
        return (
            self.collision.colliderect(rect)
        )

    def get_render_info(self) -> list:
        return [(self.type, self.collision, self.current_direction)]
