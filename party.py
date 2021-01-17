# built-in libraries
import random

# my libraries
import game_character
import util


# Represents a party of adventurers, with all of its members, as well as associated statuses like the
# amount of remaining food and water, current position in the game world, and commotion
# fields:
# _members      list of game_character.Character
# _location     util.Posn
# _commotion    int
# _food         int
# _water        int
class Party:

    # A completely random initializer. Party size and members are rolled.
    def __init__(self):
        self.members = []
        for i in range(0, random.randint(2, 7)):
            self.members.insert(i, game_character.Character())

        self._location = util.Posn(300.0, 0.0)
        self._commotion = 0
        self._food = 100
        self._water = 100

    def list_members(self):
        to_return = ""
        for i in range(0, len(self.members)):
            to_return += self.members[i].to_string() + "\n"
        return to_return

    def to_string(self):
        return str(self._location.x) + ", " + str(self._location.y) \
               + ". Food: " + str(self._food) + ", Water: " + str(self._water)

    def check_see(self, object):
        for character in self.members:
            if character.wits_check() > 10:
                util.text(character.name + " spots " + object.get_name() + "!")

    # has the party travel.
    # Returns: A string describing the travel that took place.
    # Arguments:
    # - vertical        int         1 is north, 0 is no vertical movement, -1 is south
    # - horizontal      int         1 is east, 0 is no horizontal movement, -1 is west
    # - speed           int         1 is cautious travel, 2 is standard, 3 is reckless.
    def travel(self, vertical, horizontal, speed):
        if vertical == 0 & horizontal == 0:
            return "No meaningful travel was accomplished."
        horizontal_delta = horizontal * ((0.1 * random.randint(1, 10)) * util.TRAVEL_SPEED) * (0.5 * speed)
        vertical_delta = vertical * ((0.1 * random.randint(-10, 10)) * util.TRAVEL_SPEED) * (0.5 * speed)
        self._location.x += horizontal_delta
        self._location.y += vertical_delta

        water_delta = speed * len(self. members);
        # TODO: I dunno make this more interesting and random.
        # TODO: Water and food should probably be either way bigger numbers or floats.
        self._water -= water_delta

        travel_string = ""
        if vertical != 0:
            travel_string += "Travelled {0} miles {1}. ".format("%.2f" % abs(vertical_delta),
                                                                Party.__get_ns_string(vertical))
        if horizontal != 0:
            travel_string += "Travelled {0} miles {1}.".format("%.2f" % abs(horizontal_delta),
                                                               Party.__get_ew_string(horizontal))
        return travel_string

    # Helper for travel.
    @staticmethod
    def __get_ns_string(vertical):
        if vertical == 0:
            return ""
        if vertical > 0:
            return "north"
        if vertical < 0:
            return "south"

    # Helper for travel.
    @staticmethod
    def __get_ew_string(horizontal):
        if horizontal == 0:
            return ""
        if horizontal > 0:
            return "east"
        if horizontal < 0:
            return "west"
