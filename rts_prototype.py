from prototype_1 import Prototype
from copy import deepcopy
from random import randint

class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "Knight"

        filename = "{}_{}.dat".format(self.unit_type, level)

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.name = ""
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\nLife: {1}\nSpeed: {2}\nAttack Power: {3}\nAttack Range: {4}\nWeapon: {5}".format(
            self.unit_type, self.life, self.speed, self.attack_power, self.attack_range, self.weapon
        )

    def clone(self):
        proto = deepcopy(self)
        proto.name = "Knight{}".format(randint(0,100))
        return proto

class Archer(Prototype):
    def __init__(self, level):
        self.unit_type = "Archer"

        filename = "{}_{}.dat".format(self.unit_type, level)

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\nLife: {1}\nSpeed: {2}\nAttack Power: {3}\nAttack Range: {4}\nWeapon: {5}".format(
            self.unit_type, self.life, self.speed, self.attack_power, self.attack_range, self.weapon
        )

    def clone(self):
        proto = deepcopy(self)
        proto.name = "Archer{}".format(randint(0,100))
        return proto

class Rogue(Prototype):
    def __init__(self, level):
        self.unit_type = "Rogue"

        filename = "{}_{}.dat".format(self.unit_type, level)

        with open(filename, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\nLife: {1}\nSpeed: {2}\nAttack Power: {3}\nAttack Range: {4}\nWeapon: {5}".format(
            self.unit_type, self.life, self.speed, self.attack_power, self.attack_range, self.weapon
        )

    def clone(self):
        proto = deepcopy(self)
        proto.name = "Rogue{}".format(randint(0,100))
        return proto

class Barracks(object):
    def __init__(self):
        self.units = {
            "knight": {
                1: Knight(1),
                2: Knight(2)
            },
            "rogue": {
                1: Rogue(1),
                2: Rogue(2)
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()

class ArcheryRange(object):
    def __init__(self):
        self.units = {
            "archer": {
                1: Archer(1),
                2: Archer(2)
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()

if __name__ == "__main__":
    barracks = Barracks()
    knight1 = barracks.build_unit("knight", 1)
    rogue1 = barracks.build_unit("rogue", 1)
    range = ArcheryRange()
    archer1 = range.build_unit("archer", 2)
    print("[{}] {}".format(knight1.name, knight1))
    print("[{}] {}".format(archer1.name, archer1))
    print("[{}] {}".format(rogue1.name, rogue1))
