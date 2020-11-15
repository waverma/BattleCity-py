from pygame.rect import Rect

from graphic_elements.draw_information import DrawInformation
from enums.direction import Direction
from game_logic_elements.units.unit import Unit


class Bullet(Unit):
    texture_name = "Bullet.png"

    def __init__(self, owner: Unit):
        super().__init__()
        self.collision = Rect(-1, -1, 6, 6)
        self.max_speed = 6
        self.current_direction = Direction.Up
        self.owner = owner

    def get_draw_info(self):
        result = list()

        if self.current_direction == Direction.Up:
            result.append(DrawInformation(texture_name=Bullet.texture_name,
                                          draw_rect=self.collision, texture_rotate=90 * 3))

        if self.current_direction == Direction.Down:
            result.append(DrawInformation(texture_name=Bullet.texture_name,
                                          draw_rect=self.collision, texture_rotate=90))

        if self.current_direction == Direction.Right:
            result.append(DrawInformation(texture_name=Bullet.texture_name,
                                          draw_rect=self.collision, texture_rotate=90 * 2))
        else:
            result.append(DrawInformation(texture_name=Bullet.texture_name, draw_rect=self.collision))

        return result

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

    def move_step(self, field):
        x_saved = self.collision.left
        y_saved = self.collision.top

        field.try_remove_unit(self)
        if not field.try_place_unit(self, x_saved + self.velocity[0], y_saved + self.velocity[1]):
            units = field.get_intersected_units(Rect(
                x_saved + self.velocity[0],
                y_saved + self.velocity[1],
                self.collision.width,
                self.collision.height
            ))
            field.explode(self, 34, self.collision, units)

    def on_explosion(self, field, explosion_rect: Rect):
        field.try_remove_unit(self)
