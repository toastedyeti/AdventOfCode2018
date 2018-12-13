'''
STUFF LEARNED: 
- I really wanted to try to solve this with numpy, but was not able to learn the basics in time
- Trouble with finding the right "Frame" to view the code "ZAEZRLZG"
    earlier solutions that appended coordinates to the pixel list were
    abandoned bc of printing in the console
            *********************   
            - print("@", end="") 
            ********************* 
- This solution finds coordinates within boundary ranges ymin to ymax, then xmin to xmax 
and prints an "@"
- Probably too many sources to cite on boundary management tips, but github.com/klaa97 
was the most clear and used the print("@", end="")

NEXT:
- Plot this in Numpy... animate if possible?
'''
import string
import sys
import re

class PT(object):

    def __init__(self, x, y, vx, vy):
        self.initial_settings = [x,y,vx,vy]
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def out(self):
        return [self.x, self.y]

def openInput(fname, testing = False):

    # Read, Process, Strip, Sort Input
    with open(fname) as f:
        lines = [l.strip('\n') for l in f]
        lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]
    f.close()

    if testing:
        # 19999 197,948
        for i in range(20000):
            minx = min(x + i * vx for (x, y, vx, vy) in lines)
            maxx = max(x + i * vx for (x, y, vx, vy) in lines)
            miny = min(y + i * vy for (x, y, vx, vy) in lines)
            maxy = max(y + i * vy for (x, y, vx, vy) in lines)

        print (i, maxx - minx + maxy - miny)
    print(len(lines))
    return lines

def part1(in_f):
    coords = in_f
    pts = []
    pixels = []
    l = 0
    #generate all pt objects
    for i in coords: 
        pts.append(PT(i[0],i[1],i[2],i[3]))

    for s in range(10105):
        limit =[]
        width = 100
        for i in pts:
            i.update()
        minx = min([x.getx() for x in pts])
        miny = min([y.gety() for y in pts])
        maxx = max([x.getx() for x in pts])
        maxy = max([y.gety() for y in pts])
        if minx + width >= maxx and miny + width >= maxy:
            print(s)
            pixels = [pt.out() for pt in pts]
            for y in range(miny,maxy+1):
                for x in range(minx,maxx+1):
                    if [x,y] in pixels:
                        print("@", end="")
                    else:
                        print(" ", end="")
                print("")

part1(openInput('d10.txt'))