from battle_city.engine.bonuses.fire_rapid_bonus import FireRapidBonus
from battle_city.engine.bonuses.heal_bonus import HealBonus
from battle_city.engine.bonuses.speed_up_bonus import SpeedUpBonus
from battle_city.engine.bonuses.unit_upgrade import UnitBonus
from battle_city.engine.units.armored_bot import ArmoredBot
from battle_city.engine.units.asphalt import Asphalt
from battle_city.engine.units.bonus_box import BonusBox
from battle_city.engine.units.breakable_wall import BreakableWall
from battle_city.engine.units.bullet import Bullet
from battle_city.engine.units.bush import Bush
from battle_city.engine.units.dirt import Dirt
from battle_city.engine.units.fire import Fire
from battle_city.engine.units.heal_bot import HealBot
from battle_city.engine.units.rapid_fire_bot import RapidFireBot
from battle_city.engine.units.tank import Tank
from battle_city.engine.units.tank_bot import TankBot
from battle_city.engine.units.tank_bot_spawner import TankBotSpawner
from battle_city.engine.units.unbreakable_wall import UnbreakableWall
from battle_city.engine.units.unit import Unit


registered_units = dict()
registered_units[Unit.__name__] = Unit
registered_units[ArmoredBot.__name__] = ArmoredBot
registered_units[Asphalt.__name__] = Asphalt
registered_units[BonusBox.__name__] = BonusBox
registered_units[BreakableWall.__name__] = BreakableWall
registered_units[Bullet.__name__] = Bullet
registered_units[Bush.__name__] = Bush
registered_units[Dirt.__name__] = Dirt
registered_units[Fire.__name__] = Fire
registered_units[HealBot.__name__] = HealBot
registered_units[RapidFireBot.__name__] = RapidFireBot
registered_units[Tank.__name__] = Tank
registered_units[TankBotSpawner.__name__] = TankBotSpawner
registered_units[TankBot.__name__] = TankBot
registered_units[UnbreakableWall.__name__] = UnbreakableWall

registered_bonuses = dict()
registered_bonuses[FireRapidBonus.__name__] = FireRapidBonus
registered_bonuses[HealBonus.__name__] = HealBonus
registered_bonuses[SpeedUpBonus.__name__] = SpeedUpBonus
registered_bonuses[UnitBonus.__name__] = UnitBonus


def get_unit_by(unit_class_name: str) -> Unit:
    return registered_units[unit_class_name]()


def get_bonus_by(bonus_class_name: str):
    return registered_bonuses[bonus_class_name]
