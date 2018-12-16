import os
import sys
import collections

'''
Map:
walls (#)
open cavern (.)
Goblin (G)
Elf (E)
'''
class combatant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def beacon(self):
        return (self.x, self.y)

    def recon(self):
        cx = self.x
        cy = self.y
        zones = [(cx, cy+1), (cx+1, cy), (cx, cy-1), (cx-1,cy)]


class goblin(combatant):
    def __init__(self,x,y):
       combatant.__init__(self,x,y)

class elf(combatant):
    def __init__(self,x,y):
           combatant.__init__(self,x,y)


class cave(object):
    '''
        # Map objects have elves, goblins, walls, and open space
    '''
    positions = {}
    walls = []
    combatants = []
    freespace = []


def setup(fname):
    with open(os.path.join(sys.path[0], fname), "r") as f:
        d15 = [l.strip() for l in f]
    battlefield = cave()
    for y,line in enumerate(d15):
        for x, piece in enumerate(line):
            if piece == "#":
                #battlefield.walls.append((x,y))
                # maxx = max([i[0] for i in battlefield.walls]) #31
                # maxy = max([i[1] for i in battlefield.walls]) #31
                battlefield.positions[(x,y)] = '#'
            elif piece == "G":
                #battlefield.combatants.append(goblin(x,y))
                g = goblin(x,y)
                battlefield.positions[(x,y)] = g
            elif piece == "E":
                #battlefield.combatants.append(elf(x,y))
                e = elf(x,y)
                battlefield.positions[(x,y)] = e
    return battlefield

def part1():
    battlefield = setup('d15.txt')


part1()
