import urllib.request
import csv

class TOOLS(object):

    def getInput(self, website):
        puzzleInput = urllib.request.urlopen(website)
        print(type(puzzleInput))
        print(puzzleInput)

    def openPuzzleInputCSV(self, fileName):
        puzzleOutput = []
        with open (fileName) as filein:
            puzzleInput = csv.reader(filein)
            for row in puzzleInput:
                puzzleOutput.append(row)
        return puzzleOutput

    def openPuzzleInputTXT(self, fileName):
        puzzleOutput = []
        with open(fileName) as filein:
            content = filein.readlines()
            puzzleOutput = [x.strip() for x in content]
        return puzzleOutput