import AoCTools as tools
import operator

tool = tools.TOOLS()
puzzleInput = tool.openPuzzleInputTXT("D1_input.txt")
puzzleInput = [int(x) for x in puzzleInput]

def deviceCalibration(puzzleInput):
    calibratedValue = 0
    for i in puzzleInput:
        calibratedValue += i
    return calibratedValue

def deviceCalibrationP2(puzzleInput):
    calibratedValue = 0
    freqTracker = {}
    found = False

    while found == False:
        for i in puzzleInput:
            calibratedValue += i
            if calibratedValue in freqTracker:
                freqTracker[calibratedValue] += 1
                if freqTracker[calibratedValue] == 2:
                    print("VALUE OF 2: " , calibratedValue)
                    found = True
                    break
            else:
                freqTracker[calibratedValue] = 1

deviceCalibrationP2(puzzleInput)
