from enum import Enum


class UpdateMode(Enum):
    StepOnly = 0
    IntersectOnly = 1
    StepIntersect = 2
    NoneUpdate = 4
