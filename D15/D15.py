import os
import sys
import collections

class combatant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 
    
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

    positions = {}

    def update(self):
        

def setup(fname):
    with open(os.path.join(sys.path[0], fname), "r") as f:
        d15 = [l.strip() for l in f]
    battlefield = cave()
    for y,line in enumerate(d15):
        for x, piece in enumerate(line):
            if piece == "#":
                battlefield.positions[(x,y)] = '#'
            elif piece == "G":
                g = goblin(x,y)
                battlefield.positions[(x,y)] = g
            elif piece == "E":
                e = elf(x,y)
                battlefield.positions[(x,y)] = e
    return battlefield

def part1():
    battlefield = setup('d15.txt')
    for i in range(0,20):
        battlefield.update()

part1()
