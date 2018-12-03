'''
Credit to r/u/evonfriedland for np.sum & np.all solution!
- Original soluthad a fabric class that counted each coordinate position similarly to the numpy method below.
- The fabric space was {(i,j):0 for j in range(height, width)}
- The original solution was missing much of the consumed fabric (306" only), indicating my formulas were not creating points, 
and writing values to them based on list(zip(list_compX:X+n, list_compY:Y+n)).  

New Stuff Learned:
- re.findall(r'-?\d+', i)
- numpy ranges [x:x+n, y:y+n] == var
- numpy.all return bool value iteratively after data written to array
'''

import re
import numpy as np
import AoCTools as tools

tool = tools.TOOLS()

def fabricCut(puzzleInput):
    claims = []
    untouchedClaims = []
    for i in puzzleInput:
        inst = re.findall(r'-?\d+', i)
        instN = [int(x) for x in inst]
        claims.append(instN)

    fabric = np.zeros((1000,1000))

    for row in claims:
        if len(row) > 1:
            n = row[0]
            x = row[1]
            y = row[2]
            dx = row[3]
            dy = row[4]
            fabric[x:x+dx, y:y+dy] += 1
        else:
            pass

    for row in claims:
        if len(row) > 1:
            n = row[0]
            x = row[1]
            y = row[2]
            dx = row[3]
            dy = row[4]
            if np.all(fabric[x:x+dx, y:y+dy]==1):
                untouchedClaims.append(n)
    return np.sum(fabric > 1), untouchedClaims

print(fabricCut(tool.openInput('d3.txt')))

