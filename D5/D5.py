"""
Stuff Learned:
- Combined Aa, aA,...,Zz, zZ
- re.search(combined, i): was going down a recursive path & though pattern matching would be the while control
- dict.fromkeys(string.ascii_lowercase, 0)
- set(string.ascii_lower) 
- A set is an unordered collection with no duplicate elements
- While x.replace() needs to be x = x.replace() !!!
- can string .replace().replace to same string
- slow it down and write the algorithm in comments first
"""

import AoCTools as tools
import string
import re

test = "dabAcCaCBAcCcaDA"
pI = ''
with open('d5.txt') as f:
    pI = f.readline().strip()

def pairGen():
    uC = string.ascii_uppercase
    lC = string.ascii_lowercase
    pairs = []
    for i in range(len(lC)):
        pairs.append(uC[i] + lC[i])
        pairs.append(lC[i] + uC[i])
    combined = "("+")|(".join(pairs)+")"
    return combined

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

def part1(puzzleInput):
    for i in range(len(puzzleInput) -2, -1, -1):
        cl, nl = puzzleInput[i], puzzleInput[i+1]
        if not case(cl,nl) and areSame(cl, nl):
            puzzleInput = puzzleInput[:i] + puzzleInput[i+2:]
            if i>= len(puzzleInput) - 1:
                puzzleInput = ' ' + puzzleInput
    return(len(puzzleInput.strip()))

def part2(puzzleInput):
    # For each letter in the alphabet
    alpha = string.ascii_lowercase
    ad = {}
    for i in alpha:
        pt = puzzleInput
        # Replace both upper & lower in the puzzle input
        pt = pt.replace(i,'').replace(i.upper(),'')
        # Run part1, record both letter and outcome
        ad[i] = part1(pt)
    answer = min(ad, key=ad.get)
    return answer, ad[answer]

print(part1(pI))
print(part2(pI))

