from enum import Enum, IntEnum


class UpdateMode(Enum):
    StepOnly = 0
    IntersectOnly = 1
    StepIntersect = 2
    NoneUpdate = 4


class TankTextureKind(IntEnum):
    Red = 0
    White = 1
    GreenOne = 2
    Brown = 3
    GreenTwo = 4
    Orange = 5
    GreenThree = 6


class InterfaceStage(Enum):
    InGame = 0
    MainMenu = 1
    Pause = 2
    PostGame = 3
    SinglePlayMenu = 4
    NetworkMenu = 5
    ConnectionMenu = 6
    Chat = 7
    ConnectingWaiting = 8
    PostGameAfterWin = 9


class Direction(IntEnum):
    Null = -1
    Up = 0
    Right = 1
    Down = 2
    Left = 3


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

    HealBonus = 22
    SpeedUpBonus = 23
    CoolDownBonus = 24
    DamageBonus = 25
    BonusSpawner = 26

    TankRed = 10
    TankWhite = 11
    TankGreenOne = 12
    TankBrown = 13
    TankGreenTwo = 14
    TankOrange = 15
    TankGreenThree = 16
