class MapTile:
    """Basic class for a tile on the world_map. Initialises location.""" #Is this needed? I don't know

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.location = (x, y)

class Grass(MapTile):
    def description(self):
        return "There is grass as far as the eye can see"

class Tunnel(MapTile):
    def description(self):
        return "You are in a tunnel. There is darkness as far as the eye can see."

class Start(MapTile):
    def description(self):
        return "You are in a factory warehouse. There are boxes stacked up around all of the walls."


def read_map(file):
    """Reads world_map txt file and maps each of the maptiles to a location"""

    with open(file, "r") as f:
        rows = f.readlines()

    global world_map
    world_map = [] #initialise the list that will contain the world_map
    width = len(rows[0].split("\t")) #gets the width of the world_map
    height = len(rows) #gets the height of the world_map

    for y in range (height):
        rows[y] = rows[y].replace("\n", "") #get rid of newlines
        rows[y] = rows[y].split("\t") #split words on the line by tabs
        world_map.append([]) #append an empty list to "world_map" - this contains a single row of the world_map

        for x in range(width):
            maptile = rows[y][x]
            if maptile == "":
                world_map[y].append(None)
            else:
                world_map[y].append(globals()[maptile](x, y)) #I'm not sure exactly what this does, but it allows you to call the class using a string.


def tile_at(x, y):
    """Finds the tile at (x, y)"""
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

def tile_exists(x, y):
    """Checks that the tile at (x, y) exists"""
    if tile_at(x, y) == None:
        return False
    else:
        return True

def find_exits(x, y):
    """finds all of the existing tiles around the tile at (x, y)"""
    exits = []

    if tile_exists(x, y - 1):
        exits.append("north")

    if tile_exists(x, y + 1):
        exits.append("south")

    if tile_exists(x + 1, y):
        exits.append("east")

    if tile_exists(x - 1, y):
        exits.append("west")

    return ", ".join(exits)


if __name__ == "__main__":


    read_map("map.txt")

    test = ["This", "is", "a", "list"]

    print(", ".join(test))