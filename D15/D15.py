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

    def zones(self):
        cx = self.x
        cy = self.y
        zones = [(cx, cy+1), (cx+1, cy), (cx, cy-1), (cx-1,cy)]
        return tuple(zones)

    def recon(self, enemies):
        zones = self.zones()
        targets = [c.beacon() for c in enemies if c.beacon() in zones and c.alive() is True]
        if not targets:
            return False
        else:
            return targets

    def move(self, positions, enemies, friends):
        zones = self.zones()
        e_pos = [c.beacon() for c in enemies]
        f_pos = [c.beacon() for c in friends]
        free = [c for c in zones if positions[c] != "#" and c not in e_pos and c not in f_pos]
        targets = self.recon(enemies)

    
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
            else:
                battlefield.positions[x,y] = '.'
    return battlefield

def part1():
    battlefield = setup('d15.txt')
    for i in battlefield.elves:
        i.move(battlefield.positions, battlefield.goblins, battlefield.elves)


part1()
