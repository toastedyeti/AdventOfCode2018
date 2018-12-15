'''
Stuff Learned:
- sorted((c for c in carts), key=lambda x: x.beacon())
- enumerate continutes to be useful in mapping
- os.path.join(sys.path[0], fname)
'''

#from collections import defaultdict
#from typing import List, Tuple, Dict
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
    orient_out = {1:"^", 2: ">", 3:"v", 4:"<"}
    #
    ticker = 0
    carts, tracks = setup(fname)
    crashcoords = {}
    collision = False

    while not collision:
        #print(ticker)
        crashc = []
        for c in carts:
            orient_nxt = c.orient()
            cur_x, cur_y = c.beacon()
            move_dir = orient_in[c.orient()] 
            cart_nxt = (cur_x+move_dir[0], cur_y+ move_dir[1])
            if cart_nxt not in tracks:
                print(ticker)
                print(cart_nxt)
            #print(tracks[cart_nxt] * 20)
            if tracks[cart_nxt] == '\\':
                if c.orient() == '>': #left to down
                    orient_nxt = "v"
                elif c.orient() == "<": #right to up
                    orient_nxt = '^'
                elif c.orient() == "^": #up to left
                    orient_nxt = "<"
                elif c.orient() == "v": #down to right
                    orient_nxt = ">"
            elif tracks[cart_nxt] == '/':
                if c.orient() == '>': 
                    orient_nxt = "^"
                elif c.orient() == "<": 
                    orient_nxt = 'v'
                elif c.orient() == "^": 
                    orient_nxt = ">"
                elif c.orient() == "v": 
                    orient_nxt = "<"                
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
            c.update(cart_nxt[0], cart_nxt[1], orient_nxt)
        ticker += 1
        carts = sorted((c for c in carts), key=lambda x: x.beacon())
        ticker += 1
    return cart_nxt


run_sim()