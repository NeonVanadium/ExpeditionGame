import util

# Literally any physical feature of the game world that the party could possibly see.
class Landmark:
    def __init__(self, x, y, name):
        self._location = util.Posn(x, y)
        self._name = name

    def get_location(self):
        return self._location

    def get_name(self):
        return self._name