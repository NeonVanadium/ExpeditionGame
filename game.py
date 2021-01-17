import party
import util
from landmark import Landmark
from language import Language


# This is the game model, and controls all the moving parts.

class Game:

    # Passes an hour of game time. An hour is one 'tick' of the world, the smallest possible unit of time.
    def __init__(self):
        self.party = party.Party()
        self.landmarks = []
        self.landmarks.insert(0, Landmark(300, 0, "obelisk"))

    def run(self):
        util.text("Your party gathers at the Point of No Return. Among you are:")
        util.text(self.party.list_members())
        util.text("You have brought enough food and water to last yourselves a couple of days.")
        util.text("All members report feeling healthy and prepared for the expedition.")
        util.text("Your goal: Enter the black empire, and find a city, any city. Become the first in history to go"
                  "so far and survive.\n")
        if util.confirm("Venture forth?"):
            self.open_world()
        util.text("Game over.")

    def parse_command(self, cmd):
        cmd = cmd.lower()

        speed = 2
        if "slow" in cmd or "cautious" in cmd:
           speed = 1
        elif "test" in cmd or "quick" in cmd or "reckless" in cmd:
            speed = 3

        # TODO: Write a method isolatedContains that checks if a sequence is contained as a single token,
        # TODO: ie surrounded by whitespace or the ends of a string. For things like 'se' and 'ne'
        if "northeast" in cmd or util.contains_token(cmd, "ne"):
            return self.party.travel(1, 1, speed)
        elif "northwest" in cmd or util.contains_token(cmd, "nw"):
            return self.party.travel(1, -1, speed)
        elif "southeast" in cmd or util.contains_token(cmd, "se"):
            return self.party.travel(-1, 1, speed)
        elif "southwest" in cmd or util.contains_token(cmd, "sw"):
            return self.party.travel(-1, -1, speed)
        elif "east" in cmd or util.contains_token(cmd, "e"):
            return self.party.travel(0, 1, speed)
        elif "west" in cmd or util.contains_token(cmd, "w"):
            return self.party.travel(1, 0, speed)
        elif "north" in cmd or util.contains_token(cmd, "n"):
            return self.party.travel(1, 0, speed)
        elif "south" in cmd or util.contains_token(cmd, "s"):
            return self.party.travel(-1, 0, speed)
        else:
            return self.party.travel(0, 0, 0)

    def open_world(self):
        query = ""

        while query != 'quit':
            query = input("type 'quit' to quit. Otherwise, type a direction and speed to travel.\n")
            print(self.parse_command(query))
            print(self.party.to_string())
            for landmark in self.landmarks:
                self.party.check_see(landmark)


        print("Game quit.")

    def pass_hour(self):
        pass

