# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import language

import game_character
party = []

if __name__ == '__main__':

    print("Your party gathers just south of the point of no return. Among you are:")

    for i in range(0, random.randint(2, 7)):
        party.insert(i, game_character.character())
        print(party[i].to_string())

    testomundo = ""

    while testomundo != 'q':
        testomundo = input("type q, foolish mortal")

    print("okay you can go now thank you <3")