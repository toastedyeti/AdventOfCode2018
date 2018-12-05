import urllib
import requests
import os
import csv

class TOOLS(object):

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

    def openInput(self, file):
        openFile = open(file)
        puzzleInput = openFile.read()
        puzzleInput = puzzleInput.split('\n')
        return puzzleInput
