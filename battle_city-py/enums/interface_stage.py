from enum import Enum


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
