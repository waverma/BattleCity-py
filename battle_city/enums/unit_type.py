from enum import IntEnum


class UnitType(IntEnum):
    Null = 0
    TankBot = 1
    TankPlayer = 2
    TankRival = 3
    BrickWall = 4
    IronWall = 5
    Bush = 17
    Fire = 18
    Dirt = 19
    Asphalt = 20
    PlayerSpawner = 6
    RivalSpawner = 7
    BotSpawner = 8
    EmptyBotSpawner = 21
    Bullet = 9

    TankRed = 10
    TankWhite = 11
    TankGreenOne = 12
    TankBrown = 13
    TankGreenTwo = 14
    TankOrange = 15
    TankGreenThree = 16
