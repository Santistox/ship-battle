import os
from map_generator import *
from ship_generator import *

class Battle:
    def __init__(self, width, height, debug):
        self.debug = debug # debug mode to print log on screen
        self.width = width  # width of map
        self.height = height # height of map
        self.game_map = newMap(width, height)

    def printMap(self, ppi):
        for y in range(self.height):
            for x in range(self.width):
                print("%%-%ds" % ppi % self.game_map[x][y], end="")
            print()


def main():
    os.system('clear')
    battle = Battle(30, 30, True)

    g = MapGrid(30, 30)
    g.walls = get_walls(g)
    draw_grid(g)
    print("Map generated successfully!")


if __name__ == '__main__':
    main()