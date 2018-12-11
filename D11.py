import time

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
        if i[0] + s < 300 and i[1] + y  < 300:
            if i in c:
                outsum += int(c[i])
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

def part2(serialNum):
    maxPower = 0
    gridSize = 0
    coordCapture = []
    for i in range(1,301):
        print(i, maxPower, gridSize, coordCapture)
        mp, cc = part1(serialNum, 300, i)
        if int(mp) > maxPower:
            maxPower = int(mp)
            gridSize = i
            coordCapture = [(cc)]
    return maxPower, coordCapture, gridSize

#print(part1(3463, 300, 3))
print(part2(3463))