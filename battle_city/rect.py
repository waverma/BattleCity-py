class Rect:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = self.width = w
        self.h = self.height = h

    def __eq__(self, other: 'Rect') -> bool:
        return (self.x == other.x
                and self.y == other.y
                and self.w == other.w
                and self.h == other.h)

    def collidepoint(self, x: int, y: int):
        return self.x <= x <= self.w + self.x \
               and self.y <= y <= self.h + self.y

    def colliderect(self, rect: 'Rect'):
        return (Rect.are_collide_segment(self.x, self.x + self.w - 1,
                                         rect.x, rect.x + rect.w - 1)
                and Rect.are_collide_segment(self.y, self.y + self.h - 1,
                                             rect.y, rect.y + rect.h - 1))

    @staticmethod
    def are_collide_segment(a, b, c, d):
        return a <= c <= b or d >= a >= c
