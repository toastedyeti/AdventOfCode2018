from collections import defaultdict
import parse as pr
import os, sys

'''
    - credit & thanks to u/pythondevgb on part 1
    - '_' The underscore can be used to ignore specific values in iteration
    - Was able to use parse from other problems in this solution to create tuple of first/second to depend & allow
    - all() Returns a Boolean value that indicates whether the collection contains only values that evaluate to True.

    -------------------
    - Sorting Algorithm:
        * Create dict/set by letter with every letter that it depends on
        * Create dict/set by letter with every letter that it comes before
        * Produce a set with any letter that does not have any dependencies [IHF]
        * While there are available letters [IHF]:
            * pop the last letter off the list --> CL
            * Add that letter to the final sequence
            * Get all the letters that come after CL:
                * if any of those letters is dependent on any of the letters in the sequence, and not already in the available list:
                    * add it to the available list
                * sort the available list
    -------------------

    - NEXT:
        * What other problems can this be used for?
'''
def openInput(fname):
    puzzleInput = ''
    with open(os.path.join(sys.path[0], fname)) as f:
        puzzleInput = f.readlines()
        #puzzleInput = [x.split() for x in puzzleInput]
    f.close()
    return puzzleInput

def part1(fname):
    ptrn = pr.compile("Step {} must be finished before step {} can begin.")
    instr = [(ptrn.parse(i)[0], ptrn.parse(i)[1]) for i in openInput(fname)]
    sequence_out = ''
    depend = defaultdict(set)
    allow = defaultdict(set)

    for first, second in instr:
        depend[second].add(first)
        allow[first].add(second)

    availables =  sorted(set(allow) - set(depend), reverse=True)

    while availables:
        next_avail = availables.pop()
        sequence_out += next_avail
        for x in allow[next_avail]:
            if all(j in sequence_out for j in depend[x]) and x not in availables:
                availables.append(x)
        availables.sort(reverse=True)
    print(sequence_out) #FHICMRTXYDBOAJNPWQGVZUEKLS


part1("d7.txt")