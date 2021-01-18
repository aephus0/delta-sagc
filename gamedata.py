# Class for creating new characters.
class charvals:
    def __init__(self, name, health, level, dex, str):
        self.name = name
        self.health = health
        self.level = level
        self.dex = dex
        self.str = str

# Class defining the world state
class worldvals:
    def __init__(self, room, depth, gd):
        self.room = room
        self.depth = depth
        self.gd = gd