import map
from player import *


def get_player_command():
    return input("Action: ")


def room_description(player):
    room = map.tile_at(player.x, player.y)
    return room.description()


def attempt_move(x, y, player, move_player, direction):

        if map.tile_exists(x, y):
            move_player()
            print("You go", direction)
            print(room_description(player))
            print("There are exits to the", map.find_exits(player.x, player.y))
        else:
            print("You can't go that way!")


def do_player_command(player, command):
    if command in ["n", "N"]:
        attempt_move(player.x, player.y - 1, player, player.move_north, "north")

    if command in ["s", "S"]:
        attempt_move(player.x, player.y + 1, player, player.move_south, "south")

    if command in ["e", "E"]:
        attempt_move(player.x + 1, player.y, player, player.move_east, "east")

    if command in ["w", "W"]:
        attempt_move(player.x - 1, player.y, player, player.move_west, "west")


def play():
    map.read_map("map.txt")
    player = Player()
    print("Race for the Hoover Dam!\n")
    print(room_description(player))
    print("There are exits to the", map.find_exits(player.x, player.y))

    while True:
        action_input = get_player_command()
        do_player_command(player, action_input)


if __name__ == "__main__":
    play()

