import random
from enum import Enum


class ethnicity(Enum):
    Fyuren = 0
    Harrondian = 1
    Dizaki = 2
    Jianangese = 3
    Mauali = 4
    Ked = 5
    Naalish = 6




# A character represents a game character (wow). It stores various attributes and the character's current status.
# Fields:
# - name            string
# - ethnicity       integer
# - age             integer
# - strength        integer
# - charisma        integer
# - nimbleness      integer
# - wits            integer
class character:
    def __init__(self):
        # determines how long the name should be in characters. TODO: this should really be done syllable-ways, but w/e
        name_length = random.randint(2, 10)
        self.name = ""

        # We begin with this fencepost so only the first letter of a name is capitalized.
        self.name += chr(random.randint(65, 90))
        for i in range(1, name_length):
            self.name += str.lower(chr(random.randint(65, 90)))

        self.ethnicity = random.randint(1, 6)
        self.age = random.randint(16, 110)

    def ethnicity_adj(self):
        if self.ethnicity == 0:
            return "Fyuren"
        if self.ethnicity == 1:
            return "Harrondian"
        if self.ethnicity == 2:
            return "Dizaki"
        if self.ethnicity == 3:
            return "Jian-Angese"
        if self.ethnicity == 4:
            return "Ma'uali"
        if self.ethnicity == 5:
            return "Ked"
        if self.ethnicity == 6:
            return "Naalish"

    def to_string(self):
        return "A " + str(self.age) + "-year-old " + self.ethnicity_adj() + " person named " + self.name + "."
