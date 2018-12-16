'''
Stuff Learned:
- sorted((c for c in carts), key=lambda x: x.beacon())
- enumerate continutes to be useful in mapping
- os.path.join(sys.path[0], fname)
'''

#from collections import defaultdict
#from typing import List, Tuple, Dict
import collections
import os
import sys

fname = "d13.txt"

class cart(object):
    
    inter_ctr = 0

    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.o = orientation
        self.collision = False
    
    def update(self, x, y, o):
        self.x = x
        self.y = y
        self.o = o

    def orient(self):
        return self.o

    def intersection(self):
        return self.inter_ctr

    def beacon(self):
        return (self.x, self.y)


def setup(fname):
    with open(os.path.join(sys.path[0], fname), "r") as f:
        d13 = [l.strip() for l in f]
    
    c_o = ["^", "v", ">", "<"] # cart orientations
    tr_type = ["-", "\\", "/", "+", "|"] # track types
    carts = []
    tracks = {}
    for y,line in enumerate(d13):
        for x,char in enumerate(line):
            if char in tr_type:
                tracks[(x,y)] = char
            elif char in c_o:
                carts.append(cart(x,y,char))
                if char == "^" or char == "v":
                    tracks[(x,y)] = "|"
                elif char == '<' or char == '>':
                    tracks[(x,y)] = '-'
    s_cart = sorted((c for c in carts), key=lambda x: x.beacon())
    return s_cart, tracks

def run_sim():
    # Reference Dictionaries
    orient_in = {'^':(0,-1), 'v':(0,1), '<':(-1,0), '>':(1,0)}
    #orient_out = {0:"^", 1: ">", 2:"v", 3:"<"}
    #
    ticker = 0
    carts, tracks = setup(fname)
    crashlist = []
    collision = False

    while not collision:
        for c in carts:
            orient_nxt = c.orient()
            cur_x, cur_y = c.beacon()
            move_dir = orient_in[c.orient()] 
            current_orient = c.orient()
            # coordinates of next track piece
            cart_nxt = (cur_x + move_dir[0], cur_y + move_dir[1])

            # Cart moves out of bounds ?
            if cart_nxt not in tracks:
                print(ticker)
                print(carts.index(c))
                print(c.beacon())
                print(cart_nxt)
            
            # Orient the cart
            if tracks[cart_nxt] == '\\':
                if current_orient == "^":
                    orient_nxt = ">"
                elif current_orient == ">":
                    orient_nxt = "v"
                elif current_orient == "v":
                    orient_nxt = ">"
                else:
                    orient_nxt = "^"
            elif tracks[cart_nxt] == '/':
                if current_orient == '>': 
                    orient_nxt = "^"
                elif current_orient == "^": 
                    orient_nxt = ">"
                elif current_orient == "v": 
                    orient_nxt = "<"
                else:
                    orient_nxt = "v"
            elif tracks[cart_nxt] =='+':
                if c.inter_ctr % 3 == 0:
                    #right
                    orient_nxt = "<"
                elif c.inter_ctr % 3 == 1:
                    #left
                    orient_nxt = ">"
                elif c.inter_ctr % 3 == 2:
                    #Straight
                    pass
                c.inter_ctr += 1
            elif tracks[cart_nxt] =='-' or tracks[cart_nxt] == "|":
                orient_nxt = current_orient
            
            c.update(cart_nxt[0], cart_nxt[1], orient_nxt)
            crashlist = [c.beacon for c in carts]
            if [item for item, count in collections.Counter(crashlist).items() if count > 1]:
                print([item for item, count in collections.Counter(a).items() if count > 1])
        

        carts = sorted((c for c in carts), key=lambda x: x.beacon())
        ticker += 1
    #return cart_nxt


run_sim()