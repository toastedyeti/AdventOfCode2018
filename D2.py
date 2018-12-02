import AoCTools as tools 
import string

import copy

tool = tools.TOOLS()
puzzleInput = tool.openPuzzleInputTXT("d2.txt")
testCases = ["abcde", "fghij", "klmno",  "pqrst", "fguij", "axcye", "wvxyz"]

def inventoryMgmt(puzzleInput):
    two = 0
    three = 0
    for line in puzzleInput:
        tagTrack = {x:0 for x in list(string.ascii_lowercase)}
        uno, dos, tres = 0,0,0
        for letter in line:
            if letter in tagTrack:
                tagTrack[letter] += 1
        for letter in tagTrack:
            if tagTrack[letter] == 1:
                uno += 1
            elif tagTrack[letter] == 2:
                dos += 1
            elif tagTrack[letter] == 3:
                tres += 1
            else:
                pass
        if dos >= 1:
            two += 1
        if tres >= 1:
            three += 1
    print(two*three)
    return two * three

def inventoryMgmtP2(puzzleInput):
    for line in puzzleInput:
        checkList = copy.copy(puzzleInput)
        checkList.remove(line)
        s1 = list(line)
        for i in checkList:
            s2 = list(i)
            compare = [i for i, j in zip(s1,s2) if i == j]
            if len(compare) == len(line)-1:
                print(s1)
                print(s2)
                print(puzzleInput.index(line), puzzleInput.index(i))
                print(''.join(compare))



inventoryMgmtP2(puzzleInput)

