class Armour:
    # define the constructor
    def __init__(self,
                 name: str,
                 position: int,
                 attribute: list[int]):
        self.name = name
        self.attribute = attribute
        self.position = position
        self.mobility = attribute[0] + 2
        self.resilience = attribute[1] + 2
        self.recovery = attribute[2] + 2
        self.discipline = attribute[3] + 2
        self.intellect = attribute[4] + 2
        self.strength = attribute[5] + 2
        self.total = sum(attribute)


class Guardian:
    def __init__(self,
                 exotic: Armour):
        self.exotic = exotic
        self.name = exotic.name
        self.position = exotic.position
        self.mobility = exotic.mobility
        self.resilience = exotic.resilience
        self.recovery = exotic.recovery
        self.discipline = exotic.discipline
        self.intellect = exotic.intellect
        self.strength = exotic.strength
        self.legendary = []

    def add_attribute(self, armour: Armour):
        self.mobility += armour.mobility
        self.resilience += armour.resilience
        self.recovery += armour.recovery
        self.discipline += armour.discipline
        self.intellect += armour.intellect
        self.strength += armour.strength

    def clear_attribute(self):
        self.mobility = self.exotic.mobility
        self.resilience = self.exotic.resilience
        self.recovery = self.exotic.recovery
        self.discipline = self.exotic.discipline
        self.intellect = self.exotic.intellect
        self.strength = self.exotic.strength

    def load_armour(self, armour: Armour):
        if len(self.legendary) < 3:
            self.legendary.append(armour)
            self.add_attribute(armour)

    def clear_armour(self, armour: Armour):
        self.legendary.remove(armour)
        self.mobility -= armour.mobility
        self.resilience -= armour.resilience
        self.recovery -= armour.recovery
        self.discipline -= armour.discipline
        self.intellect -= armour.intellect
        self.strength -= armour.strength

    def print_attribute(self):
        print("Mobility: ", self.mobility)
        print("Resilience: ", self.resilience)
        print("Recovery: ", self.recovery)
        print("Discipline: ", self.discipline)
        print("Intellect: ", self.intellect)
        print("Strength: ", self.strength)
        for armour in self.legendary:
            print(armour.position, armour.name, armour.attribute)
        print("=====================================")


EXO_Getaway_artist_old = Armour("Getaway artist", 1, [20, 13, 15, 18, 18, 4])
EXO_Getaway_artist_new = Armour("Getaway artist", 1, [4, 13, 22, 20, 8, 11])
EXO_Getaway_artist_2 = Armour("Getaway artist", 1, [12, 19, 9, 26, 9, 4])
EXO_Getaway_artist_3 = Armour("Getaway artist", 1, [9, 5, 26, 12, 8, 18])
EXO_Speaker_sight = Armour("Speaker's sight", 0, [12, 4, 23, 24, 12, 13])

getaway_artist = Guardian(EXO_Getaway_artist_3)
speaker_sight = Guardian(EXO_Speaker_sight)

HELMET_LIST = [
    Armour("TAH/89", 0, [2, 29, 2, 30, 2, 2]),
    Armour("OC/90", 0, [2, 16, 16, 20, 14, 4]),
    # Armour("SH/88", 0, [15, 6, 12, 2, 2, 29]),
]
GAUNTLET_LIST = [
    Armour("TAG/89", 1, [2, 26, 16, 22, 9, 2]),
    Armour("NWG/67", 1, [7, 2, 24, 26, 2, 6]),
    Armour("BRG/76", 1, [2, 17, 23, 26, 2, 6]),
    Armour("NWG/86", 1, [6, 23, 2, 29, 2, 2]),
]
CHEST_LIST = [
    # Armour("UER/71", 2, [6, 2, 26, 24, 6, 2]),
    Armour("不羁-赛季-89", 2, [2, 22, 9, 16, 2, 16]),
    Armour("不羁-不羁-89", 2, [2, 12, 19, 16, 16, 2]),
    Armour("UER/78", 2, [12, 2, 20, 16, 12, 6]),
    # Armour("UER/66A", 2, [2, 8, 23, 10, 21, 2]),
    Armour("不羁-笃学-88", 2, [2, 9, 22, 23, 2, 8]),
    Armour("真相-87", 2, [2, 23, 6, 26, 2, 6]),
    Armour("不羁-68", 2, [12, 2, 20, 16, 12, 6]),
    Armour("不羁-66", 2, [6, 2, 26, 24, 6, 2]),
    Armour("布瑞-67", 2, [2, 29, 2, 6, 26, 2]),
]
LEG_LIST = [
    # Armour("NWP/85", 3, [2, 2, 28, 23, 2, 6]),
    Armour("NWP/89", 3, [2, 30, 2, 21, 10, 2]),
    Armour("UEB/90", 3, [2, 6, 26, 6, 16, 12]),
    Armour("UEB/77", 3, [2, 20, 22, 22, 9, 2]),
    Armour("VB/87", 3, [6, 2, 25, 14, 8, 10]),
    Armour("不羁-78", 3, [2, 30, 2, 16, 2, 16]),
    Armour("不羁-67", 3, [8, 23, 2, 12, 20, 2])
]


def iterate_armour(guardian: Guardian):
    armour_list = [HELMET_LIST, GAUNTLET_LIST, CHEST_LIST, LEG_LIST]
    # remove index 2 of armour_list
    armour_list.pop(guardian.position)
    for amour0 in armour_list[0]:
        guardian.load_armour(amour0)
        for amour1 in armour_list[1]:
            guardian.load_armour(amour1)
            for amour2 in armour_list[2]:
                guardian.load_armour(amour2)
                if (guardian.resilience % 10 + guardian.recovery % 10 + guardian.discipline % 10 < 15
                        and (guardian.resilience % 10 != 5 and guardian.resilience % 10 != 6)
                        and (guardian.recovery % 10 != 5 and guardian.recovery % 10 != 6)
                        and (guardian.discipline % 10 != 5 and guardian.discipline % 10 != 6)
                        and guardian.resilience + guardian.recovery + guardian.discipline > 230)\
                        and guardian.resilience < 95 and guardian.discipline < 95 and guardian.recovery > 50:
                    print("=====================================")
                    guardian.print_attribute()
                guardian.clear_armour(amour2)
            guardian.clear_armour(amour1)
        guardian.clear_armour(amour0)


if __name__ == '__main__':
    iterate_armour(getaway_artist)
    print("=====================================")
