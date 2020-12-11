import os

from battle_city.game_loop import GameLoop
from battle_city.graphic_elements.graphic_utils import GraphicUtils
from battle_city.graphic_elements.texture_provider import TextureProvider

# TODO убрать -py из названия пакетов [сделано]
# TODO 1) четыре типа врагов(
#  бронированный(2 хп/ это текущий),
#  простой(1 хп),
#  скорострельный(1 хп, более скорострельный),
#  хилящийся танк(по истечении 3 секунд между получением урона, хилит себя)
#  ) [сделано]
#
# TODO 2) новые препятствия(
#  кирпич,
#  бетон,
#  кусты(ковозь них можно ехать),
#  текстура урона(огонь(гореть) или вода(тонуть)),
#  грязь(замедляет)
#  ) [сделано]
#
# TODO ДОБАВИТЬ НОВЫЕ ТЕКСТУРЫ В ГРАФИКУ. [сделано]
# TODO починить рендеринг [сделано]
# TODO Изменить метод передвижения так,
#  чтобы можно было приближаться в упор. [сделано]
#
# TODO 3) четыре уровня(
#  чем выше, тем разнообразнее.
#  лимит у спавнера(
#   например, каждый спавнер должен обязательно заспавнить разные типы танков
#   )
#  ) [сделано]
#
# TODO 4) внутриигровая табличка с показателями(
#  бонусы, очки, жизнь, скорость
#  ) [сделано, частично]
#
# TODO 5) чит коды(последовательность кнопок, как в ГТА:СА)(
#  хилл,
#  увилечение урона,
#  неуязвимость
#  ) [сделано]
#
# TODO убрать магические числа из логики в,
#  например, класс с константами игрового мира [сделано]
# TODO убрать константы графики в graphic_utils [сделано]
# TODO вынести игровые назписи дальше в рендер. [сделано]
# TODO ИСПРАВИТЬ БАГ С ПОЛУЧЕННЫМИ ОЧКАМИ [сделано]
# TODO в файле томл удалить coverage report [сделано]

if __name__ == "__main__":
    game_loop = GameLoop(
        GraphicUtils.DEFAULT_CLIENT_SIZE[0],
        GraphicUtils.DEFAULT_CLIENT_SIZE[1],
    )

    TextureProvider.set_textures(
        os.path.normpath(
            os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir
        )
    )

    game_loop.run()
