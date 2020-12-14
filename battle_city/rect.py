class Rect:
    def __init__(self, x: int = 0, y: int = 0, w: int = 0, h: int = 0):
        self.x = x
        self.y = y
        self.w = self.width = w
        self.h = self.height = h

    def __eq__(self, other: "Rect") -> bool:
        return (
            self.x == other.x
            and self.y == other.y
            and self.w == other.w
            and self.h == other.h
        )

    def is_valid(self) -> bool:
        return not (self.x is None
                    or self.y is None
                    or self.w is None
                    or self.h is None)

    def set_x(self, x: int):
        self.x = x
        return self

    def set_y(self, y: int):
        self.y = y
        return self

    def set_width(self, width: int):
        self.w = self.width = width
        return self

    def set_height(self, height: int):
        self.h = self.height = height
        return self

    def collidepoint(self, x: int, y: int):
        return (
            self.x <= x <= self.w + self.x and self.y <= y <= self.h + self.y
        )

    def colliderect(self, rect: "Rect"):
        return Rect.are_collide_segment(
            self.x, self.x + self.w - 1, rect.x, rect.x + rect.w - 1
        ) and Rect.are_collide_segment(
            self.y, self.y + self.h - 1, rect.y, rect.y + rect.h - 1
        )

    @staticmethod
    def are_collide_segment(a, b, c, d):
        return a <= c <= b or d >= a >= c
