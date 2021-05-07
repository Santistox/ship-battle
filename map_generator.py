from random import randint, choice


class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = [] # or initialize it with walls using get_walls()


# print map
def draw_grid(graph, width=2):
    for y in range(graph.height):
        for x in range(graph.width):
            if (x, y) in graph.walls:
                print("%%-%ds" % width % '#', end="")
            else:
                print("%%-%ds" % width % '.', end="")
        print()


# Game map generation
# g - MapGrid class
# ptc - generation density
def get_walls(g, pct=.1):
    gmap = []
    for i in range(int(g.height*g.width*pct)//2):
        x = randint(1, g.width-1)
        y = randint(1, g.height-2)
        gmap.append((x, y))
        gmap.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
    return gmap

g = MapGrid(30, 30)
g.walls = get_walls(g)
draw_grid(g)