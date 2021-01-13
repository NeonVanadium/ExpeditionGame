# contains various simple classes and methods. Python might have a built in version of some of these, but I'm making
# them myself bc I want to and you cannot stop me
from enum import Enum
from language import Language

# #
# Static Finals. Apparently python doesn't have final variables. Ok. These shouldn't be changed.
# #

# The default speed of travel, in mph
TRAVEL_SPEED = 5
OUTPUT_MODE = 'c'

Harrondian = Language("Harrondian",
                      ['m', 'n', 'p', 'b', "p'", 't', 'd', "t'", 'k', 'g', "k'", 'dz', "ts'", 'mv', 's', 'nz', 'h',
                       'r',
                       'l'],
                      ['a', 'e', 'i', 'o'],
                      0, 1, 1, 1, 0, 2)
Naal_Ayan = Language("Nal Ayan",
                     ['m', 'n', 'p', 'b', 't', 'd', 'k', 'g', 'z', 's', 'sh', 'zh', 'v', 'h', 'r',
                      'l', 'y'],
                     ['a', 'e', 'i', 'o', 'u'],
                     0, 2, 1, 3, 0, 2)
Dizaki = Language("Dizaki",
                  ['m', 'n', 'p', 'b', 't', 'd', 'k', 'g', 'z', 's', 'sh', 'j', 'v', 'h', 'r',
                   'l', 'y'],
                  ['a', 'e', 'i', 'o', 'u'],
                  1, 1, 1, 1, 0, 1)
Jianangese = Language("Jian-angese",
                      ['m', 'n', 'p', 'b', 't', 'd', 'k', 'g', 's', 'sh', 'zh', 'w', 'h', 'r',
                       'l', 'ng', 'y', "'"],
                      ['a', 'e', 'i', 'o', 'u'],
                      0, 1, 1, 3, 0, 1)
Ked = Language("Ked",
               ['m', 'n', 'p', 'b', 't', 'd', 'q', 's', 'z', 'sh', 'zh', 'w', 'hh', 'kh', 'r',
                'l', 'y', "'"],
               ['a', 'e', 'i', 'o', 'u'],
               0, 1, 0, 3, 1, 3)
Mauali = Language("Mauali",
                  ['m', 'n', 'p', 'b', 't', 'd', 'q', 's', 'z', 'ch', 'll', 'w', 'h', 'r',
                   'l', 'y', "'"],
                  ['a', 'e', 'i', 'o', 'u'],
                  0, 2, 0, 3, 1, 3)


# #
# Value classes
# #

# position, or location, on a 2d grid.
# Fields:
# x     float
# y     float
class Posn:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# #
# Utility methods
# #

# abstract method for yes / no prompts.
# Returns boolean
# args:
# prompt    string      the message to display with the prompt. "y/n" is added automatically.
def confirm(prompt):
    answer = None
    while answer is None:
        response = input("{0} (y/n)\n".format(prompt))
        if response.lower() == 'y' or response.lower() == 'yes':
            return True
        if response.lower() == 'n' or response.lower() == 'no':
            return False
        print("Response invalid.")


# Allows easier expanding into graphical text if I choose to do so later.
def text(string):
    if OUTPUT_MODE == 'c':  # c for console
        print(string)  # TODO: auto-wrapper


# a contains method that only returns true if the sequence is surrounded by whitespace
# returns:   boolean
# args:
# string    string      the string to be searched for the token
# token     string      the token being searched for in the main string
def contains_token(string, token):
    if token not in string:
        return False
    start_index = string.index(token)
    end_index = start_index + len(token) - 1
    return (start_index == 0 or string[start_index - 1] == " ") and \
           (end_index == len(string) - 1 or string[end_index + 1] == " ")


# # #
# Everything below here is currently unused.
# # #

# Represents the directions of a compass.
class Direction(Enum):
    North = 1
    Northeast = 2
    East = 3
    Southeast = 4
    South = 5
    Southwest = 6
    West = 7
    Northwest = 8

    # Helper for travel.
    @staticmethod
    def __get_direction_string(horizontal, vertical):
        if vertical == 1:
            if horizontal == 1:
                return "northeast"
            elif horizontal == 2:
                return "northwest"
            else:
                return "north"
        elif vertical == -1:
            if horizontal == 1:
                return "southeast"
            elif horizontal == 2:
                return "southwest"
            else:
                return "south"
        elif horizontal == 1:
            return "east"
        elif horizontal == -1:
            return "west"
