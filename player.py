class Player:
    """Class for the player. Sets location of player to (0, 0) and sets health to 10. The mechanics by which
    movement happens are going to be dealt with here"""

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)