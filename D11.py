import time
import numpy as np

'''
Stuff Learned:
    - I would not have thought to subtract the size from the range in P2
    - np.sum & grid[] !!!!!
'''


def hundreds(numbers):
    one = numbers%10
    tens = (numbers/10)%10
    hundreds = (numbers/100)%10
    thousands = numbers / 1000
    return hundreds

def generateGrid(serialNum, size):
    xc = [x for x in range(1, size+1)]
    yc = [y for y in range(1, size+1)]
    rackIDC = 10
    coords = []
    coordD = {}
    for x in xc:
        for y in yc:
            coords.append([x,y])
    for i in coords:
        i.append(i[0]+rackIDC)
        i.append(i[2]*i[1])
        i[3] += serialNum
        i[3] *= i[2]
        if hundreds(i[3]) > 0:
            i[3] = hundreds(i[3])
        else:
            i[3] = 0
        i[3] -= 5
        coordD[(i[0], i[1])] = i[3]
    return coordD

def cellValue(x,y,c,s):
    r = []
    outsum = 0
    xr = [i for i in range(x, x+s)]
    yr = [i for i in range(y, y+s)]
    for x in xr:
        for y in yr:
            r.append((x,y))
    for i in r:
            if i in c:
                # this may produce incorrect for P1, as it was altered (incorrectly) for part2
                # attempting to set a boundary to skip if the grid looks outside of
                if i[0] + s <= 300 and i[1] + s  <= 300:
                    outsum += int(c[i])
                else:
                    pass
    return outsum

def part1(serialNum, size, s):
    coords = generateGrid(serialNum, size)
    maxPower = 0
    coordCapture = []
    r = [(i) for i in coords]
    for i in r:
        os = cellValue(i[0], i[1], coords, s)
        if os > maxPower:
            maxPower = os
            coordCapture = [(i[0], i[1])]
    return maxPower, coordCapture

def power(X,Y,S):
    # u/jonathan_paulson
    rack_id = X+10
    power = rack_id * Y + S
    power = power * rack_id
    power = (power/100)%10
    power -= 5
    return power

def part2(serialNum): #-- Does not give the right solution
    maxPower = 0
    gridSize = 0
    coordCapture = []
    # Numpy ... not mine... using to learn
    grid = np.fromfunction(lambda x, y :power(x, y, serialNum), (300, 300))
    for size in range(3,300): # 3-300 starts from part1() grid size
        if not size % 10: # nice trick to print 10 count tracking
            print(size)
        for x in range(300-size): 
            for y in range(300-size):
                if y>size-1 and x>size-1: #again u/jonathan_paulson 
                    mp = np.sum(grid[x:x+size, y:y+size])
                    if mp > maxPower:
                        maxPower = mp
                        coordCapture = [x,y]
                        gridSize = size
    return  coordCapture, gridSize

        # Inefficient -- would take over 1-2 hours to run
        # for i in range(1,301):
            # mp, cc = part1(serialNum, 300, i)
            # if int(mp) > maxPower:
            #     maxPower = int(mp)
            #     gridSize = i
            #     coordCapture = [(cc)]

#print(part1(3463, 300, 3))
print(part2(3463))