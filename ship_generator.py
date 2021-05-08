
from random import randint, choice

class ShipGrid:
    def __init__(self):
        # {'class 1': qty, 'class 2': qty, 'class 3': qty, 'class 4': qty,}
        # class 1 - small 1-cell ship
        # class 2 - medium 2-cell ship
        # class 3 - large 3-cell ship
        # class 4 - extra large 4-cell ship
        self.qty = {} # quantity of ships
        self.ships = [] # location of ships on the map of each class

# print map
def newMap(width, height, ptc):
    gmap = [['.']*width]*height
    bmap = []
    for i in range(int(height*width*ptc)//2):
        x = randint(1, width-1)
        y = randint(1, height-2)
        gmap[x][y] = '#'
        gmap[x + choice([-1, 0, 1])][y + choice([-1, 0, 1])] = '#'
        # bmap.append((x, y))
        # bmap.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
    print(bmap)
    # for y in range(height):
    #     for x in range(width):
    #         if (x, y) in bmap:
    #             gmap[x][y] = '#'
    #             print("%%-%ds" % 2 % gmap[x][y], end="")
    #             # print("%%-%ds" % 2 % '#', end="")
    #         else:
    #             gmap[x][y] = '-'
    #             print("%%-%ds" % 2 % gmap[x][y], end="")
    #             # print("%%-%ds" % 2 % '.', end="")
    #     print()
    # if ptc:
    #     for x in range(width):
    #         for y in range(height):
    #             if (x, y) in bmap:
    #                 gmap[x][y] = '#'
                
    for row in gmap:
        for elem in row:
            print("%%-%ds" % 2 % elem, end="")
        print()     
        # print(row)
    print(gmap)

# newMap(30,30, 0.1)



