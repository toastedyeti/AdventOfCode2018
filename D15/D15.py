import os
import sys
import collections

class combatant:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        self.hp = 200

    def getid(self):
        return self.id

    def beacon(self):
        return (self.x, self.y)

    def alive(self):
        return self.hp > 0

    def recon(self, enemies):
        cx = self.x
        cy = self.y
        zones = [(cx, cy+1), (cx+1, cy), (cx, cy-1), (cx-1,cy)]
        for i in zones:
            targets = [i for i in enemies if i.type != self.type and i.alive() == True]
        return targets
    
    
class goblin(combatant):
    type = "G"

class elf(combatant):
    type = "E"

class cave(object):
    positions = {}
    elves = []
    goblins = []


def setup(fname):
    with open(os.path.join(sys.path[0], fname), "r") as f:
        d15 = [l.strip() for l in f]
    battlefield = cave()
    uid = 0
    for y,line in enumerate(d15):
        for x, piece in enumerate(line):
            if piece == "#":
                battlefield.positions[(x,y)] = '#'
            elif piece == "G":
                g = goblin(x,y, uid)
                battlefield.positions[(x,y)] = '.'
                battlefield.goblins.append(g)
                uid += 1
            elif piece == "E":
                e = elf(x,y,uid)
                battlefield.positions[(x,y)] = '.'
                battlefield.elves.append(e)
                uid += 1
    return battlefield

def part1():
    battlefield = setup('d15.txt')
    for i in battlefield.elves:
        print(i.id, i.recon(battlefield.goblins),"\n")
    # print(battlefield.positions)
    # print(battlefield.elves)
    # print(battlefield.goblins)

part1()
