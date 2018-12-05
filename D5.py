import AoCTools as tools
import string

tool = tools.TOOLS()

test = "dabAcCaCBAcCcaDA"
pI = tool.openInput('d5.txt')
pI1 = [l for l in pI[0]]
pI2 = str(pI[0])

def case(l1, l2):
    if l1.islower() == l2.islower() or l1.isupper() == l2.isupper():
        return True
    else:
        return False

def areSame(l1, l2):
    if l1.lower() == l2.lower():
        return True
    else:
        return False 

def part1(pI):
    cL = 0  # Current Letter
    nL = 0  # Next Letter

    for l in range(len(pI)-1):
        cL = pI[l]
        nL = pI[l+1]
        newStr = ''
        if areSame(cL, nL) and not case(cL, nL):
            i = pI.index(cL)
            j = pI.index(nL)
            newStr = pI[:i] + pI[j+1:]
            return part1(newStr)
part1(test)