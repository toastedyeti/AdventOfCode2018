from collections import defaultdict

'''
This is not my code or complete, im just trying to see how to solve this
-  '_' The underscore can be used to ignore specific values in iteration
FHICMRTXYDBOAJNPWQGVZUEKLS
'''

def openInput(fileName):
    puzzleInput = ''
    with open(fileName) as f:
        puzzleInput = f.readlines()
        puzzleInput = [x.split() for x in puzzleInput]
    f.close()
    return puzzleInput

def part1():
    inst = [(x[1], x[7]) for x in openInput('d7_test.txt')]
    ordered = ''
    depend = defaultdict(set)
    allow = defaultdict(set)

    for first, second in inst:
        depend[second].add(first)
        allow[first].add(second)
    availables =  sorted(set(allow) - set(depend), reverse=True)

    #Part1
    while availables:
        next_available = availables.pop()
        ordered+=next_available
        for el in allow[next_available]:
            if all(dep in ordered for dep in depend[el]) and el not in availables:
                availables.append(el)
        availables.sort(reverse=True)

part1()