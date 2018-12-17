import re
import os, sys
from collections import defaultdict

fname = 'd17.txt'

class element(object):
    glyp = "*"

    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def plot(self):
        return (self.x, self.y)
    
    def kind(self):
        return type(self)

    def around(self):
        u = (self.x, self.y -1)
        d = (self.x, self.y+1)
        l = (self.x-1, self.y)
        r = (self.x+1, self.y)
        return u,d,l,r
    
    def pos_update(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def icon(self):
        return self.glyph

class spring(object):
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.glyph = "+"
    
    def stream(self):
        #generate water
        raise NotImplemented

class water(element):
    glyph = "|"
    flow = True
    def pathfind(self, grid):
        #water flows down first then left and right
        g = grid
        while self.flow:
            u,d,l,r = self.around()
            cur_pos = self.plot()
            if type(g[d]) != clay and not g[d].flow and 1 <= g[d].plot()[1] <= maxy:
                g[d] = self
                self.pos_update(d)
                g[cur_pos] = '.'
            
            if type(g[d]) != clay and type(g[d]) == water and g[d].flow != False:
                pass
            

            

class clay(element):
    glyph = "#"

class sand(element):
    glyph = "."

def setup(fname):
    claycoords = []
    grid = defaultdict(lambda:'.')
    
    for line in open(os.path.join(sys.path[0], fname)).read().splitlines():
        a,b = line.split(',')
        if a[0] == "x":
            x = int(a.split("=")[1])
            y1,y2 = map(int,b.split('=')[1].split('..'))
            for y in range (y1, y2+1):
                claycoords.append((x,y))
        else:
            y = int(a.split('=')[1])
            x1,x2 = map(int,b.split('=')[1].split('..'))
            for x in range(x1,x2):
                claycoords.append((x,y))
    miny = min(claycoords, key=lambda c:c[1])[1]
    maxy = max(claycoords, key=lambda c:c[1])[1]
    minx = min(claycoords, key=lambda c:c[0])[0]
    maxx = max(claycoords, key=lambda c:c[0])[0]
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            grid[(x,y)]
    for i in claycoords:
        grid[i] = clay(i)
    
    spc = (500,0)
    grid[spc] = spring(spc)

    return grid, miny, maxy, minx, maxx

def print_grid(grid, x1=300, x2=700, y1=0, y2=1000):
    g = grid
    print('\n'.join(''.join(g[(x,y)].glyph) for x in range(x1, 1 + x2)) for y in range(y1, 1 + y2))

def part1(fname):
    grid, miny, maxy, minx, maxx = setup(fname)
    print_grid(grid)

part1(fname)