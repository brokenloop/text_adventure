class Monster:
    """Monster with health"""

    def __init__(self, name, health):
        self.name = name
        self.health = health


    def display_health(self):
        print(self.health)


    def reduce_health(self, damage):
        self.health -= damage

        if self.health <= 0:
            print (self.name, "is dead!")
        else:
            print ("Goblin has", self.health, "hp")


class Weapon:
    """Weapon with attack damage"""

    def __init__(self, damage):
        self.damage = damage

    #reduces the health of the target by the amount of damage that the weapon has
    def hit(self, target):
        target.reduce_health(self.damage)


class MapTile:
    """Basic class for a tile on the world_map. Initialises location."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (x, y)


class Player:
    """Class for the player. Sets location of player to (0, 0) and sets health to 10."""

    def __init__(self):
        self.location = (0, 0)
        self.health = (10)


def make_map(x, y):
    """
    Creates the list of locations. For every line of the world_map it generates a list of x and y values
    So we end up with a list of lists. I'm going to try to make it so that these are mapped to MapTiles
    """

    global location
    location = []

    for i in range(x):
        line = []
        for j in range(y):
            line.append((i, j))

        location.append(line)


def read_map(file):
    """Reads world_map txt file and maps each of the maptiles to a location"""

    with open(file, "r") as f:
        rows = f.readlines()

    map = {}
    width = len(rows[0].split("\t")) #gets the width of the world_map
    height = len(rows) #gets the height of the world_map
    counter = 0  # this is a hacky solution to the fact that we need to count backwards, but still need to access the string as if we were counting forwards.

    for i in range ((height - 1), -1, -1): #This has to count backwards, since we begin reading the list from the top
        rows[counter] = rows[counter].replace("\n", "") #get rid of newlines
        rows[counter] = rows[counter].split("\t") #split words on the line by tabs
        for j in range(width):
            tile = rows[counter][j]
            map.update({(i, j):tile}) #add coordinates to the dictionary in the form "(x, y):maptile"
        counter += 1

    print(map)
    #print(width, height)


read_map("world_map.txt")

