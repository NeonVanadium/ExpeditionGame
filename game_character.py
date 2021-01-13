import random
import language
from enum import Enum

class ethnicity(Enum):
    Fyuren = 0
    Harrondian = 1
    Dizaki = 2
    Jianangese = 3
    Mauali = 4
    Ked = 5
    Naalish = 6

    def get_language(self):
        if self == ethnicity.Harrondian:
            return language.Harrondian
        elif self == ethnicity.Dizaki:
            return language.Dizaki
        elif self == ethnicity.Jianangese:
            return language.Jianangese
        elif self == ethnicity.Mauali:
            return language.Mauali
        elif self == ethnicity.Ked:
            return language.Ked
        elif self == ethnicity.Naalish:
            return language.Naal_Ayan

    # Returns a string containing the adjective of this ethnicity
    def adj(self):
        if self == ethnicity.Harrondian:
            return "Harrondian"
        elif self == ethnicity.Dizaki:
            return "Dizaki"
        elif self == ethnicity.Jianangese:
            return "Jian-Angese"
        elif self == ethnicity.Mauali:
            return "Ma'uali"
        elif self == ethnicity.Ked:
            return "Ked"
        elif self == ethnicity.Naalish:
            return "Naalish"


# defines a biological sex.
class sex(Enum):
    female = 0
    male = 1
    intersex = 2

    def get_adj(self):
        if self == sex.female:
            return "female"
        if self == sex.male:
            return "male"
        if self == sex.intersex:
            return "intersex"


# defines a gender identity.
class gender(Enum):
    woman = 0
    man = 1
    nb = 2

    # gets the noun for the gender
    def get_noun(self):
        if self == gender.woman:
            return "woman"
        if self == gender.man:
            return "man"
        if self == gender.nb:
            return "enby"

    # returns the subject pronoun for the gender
    def get_subj_pron(self):
        if self == gender.woman:
            return "she"
        elif self == gender.man:
            return "he"
        else:
            return "they"

    # returns the object pronoun for the gender
    def get_obj_pron(self):
        if self == gender.woman:
            return "her"
        elif self == gender.man:
            return "him"
        else:
            return "them"

    # returns the possessive pronoun for the gender
    def get_pos_pron(self):
        if self == gender.woman:
            return "her"
        elif self == gender.man:
            return "his"
        else:
            return "their"

    # returns the reflexive pronoun for the gender
    def get_ref_pron(self):
        if self == gender.woman:
            return "herself"
        elif self == gender.man:
            return "himself"
        else:
            return "themself"


# A character represents a game character (wow). It stores various attributes and the character's current status.
# Fields:
# - name            string
# - sex             integer
# - ethnicity       integer
# - age             integer
# - weight          integer
# - is_mage         boolean
# - vitality        integer
# - wits            integer
class Character:
    def __init__(self):
        self.ethnicity = Character.get_ethnicity(random.randint(1, 6))
        self.age = random.randint(16, 110)

        self.name = self.ethnicity.get_language().create_word()

        self._gen_sex_and_gender()
        self.__gen_weight()
        self.vitality = random.randint(1, 10)
        self.wits = random.randint(1, 10)

    @staticmethod
    def get_ethnicity(num):
        if num == 0:
            return ethnicity.Fyuren
        if num == 1:
            return ethnicity.Harrondian
        if num == 2:
            return ethnicity.Dizaki
        if num == 3:
            return ethnicity.Jianangese
        if num == 4:
            return ethnicity.Mauali
        if num == 5:
            return ethnicity.Ked
        if num == 6:
            return ethnicity.Naalish

    def to_string(self):
        return "A " + str(self.age) + "-year-old " + self.ethnicity.adj() + " " + self.gender.get_noun() + " named " \
               + self.name + ". " \
               + self.gender.get_subj_pron().capitalize() + " weighs " + str(self._weight) + " pounds."

    # Below here are helper methods for certain aspects of character generation

    # generates biological sex. A roll of 100 indicates some degree of biological intersex.
    def __gen_sex(self):
        roll = random.randint(1, 100)
        if roll < 50:
            self.sex = sex.female
        elif roll == 100:
            self.sex = sex.intersex
        else:
            self.sex = sex.male

    # generates a gender indentity. Most characters whose sex are male or female identify with as a man or woman,
    # respectively. One in sixty are assigned a random identity. Intersex characters are always assigned a random
    # identity. REQUIRES THAT SEX WAS GENERATED FIRST
    def __gen_gender(self):
        if self.sex is None:
            raise TypeError("Sex was None. A sex must be generated before gender is generated.")
        # intersex characters skip this block
        if self.sex != sex.intersex:
            roll = random.randint(1, 60)
            if roll != 60:
                if self.sex == sex.male:
                    self.gender = gender.man
                elif self.sex == sex.female:
                    self.gender = gender.woman
                return
        # if we reach here, we assign an identity at random
        roll = random.randint(1, 3)
        if roll == 1:
            self.gender = gender.woman
        elif roll == 2:
            self.gender = gender.man
        else:
            self.gender = gender.nb

    # generates a character's weight. Based on sex.
    def __gen_weight(self):
        if self.sex is None:
            raise TypeError("Sex was none. Generate sex first.")
        if self.sex == sex.male:
            self._weight = random.randint(130, 250)
        if self.sex == sex.female:
            self._weight = random.randint(100, 220)
        if self.sex == sex.intersex:
            self._weight = random.randint(100, 250)

    def _gen_sex_and_gender(self):
        self.__gen_sex()
        self.__gen_gender()
