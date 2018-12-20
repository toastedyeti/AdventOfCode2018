'''
Stuff Learned:
- So many of the other AOC challenges needed a recursive solution, and my knowledge is shaky... thanks to u/sciyoshi for the clear solution
- Recursion requires determining the trivial case, and if that cannot be implemented, passing a smaller portion of the problem down the line
- Here the trivial case is the (A) no children and sum metadata for no children.  The function returns total and the remaining unparsed data

Next:
More recursion exercises from "thinking like a programmer"
'''

import sys, os

dt = [2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2]

def openInput(fname):
    out = []
    for i in open(os.path.join(sys.path[0], fname)).read().strip('\n').split(" "):
        out.append(int(i))
    return out

data = openInput('d8.txt')

def part1(data):
    c, m = data[:2]
    data = data[2:]
    total = 0

    for i in range(c):
        t, data = part1(data)
        total += t
    
    total += sum(data[:m])

    if c == 0:
        return (total, data[m:])
    else: 
        return (total, data[m:])

t, data = part1(dt)
print(t)

def part2(data):
    c, m = data[:2]
    data = data[2:]
    total = 0
    scores = []

    for i in range(c):
        t, data,v = part2(data)
        total += t
        scores.append(v)
    
    total += sum(data[:m])

    if c == 0:
        return (total, data[m:], sum(data[:m]))
    else:
        v = sum(scores[k-1] for k in data[:m] if k > 0 and k<= len(scores))
        return (total, data[m:], v)

t, data, v = part2(dt)
print(t,v)
