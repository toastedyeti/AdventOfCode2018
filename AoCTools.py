import urllib
import requests
import os
import csv

class TOOLS(object):

    def getInput(self, website):
        r = requests.get(website,timeout=5)
        print(r.status_code)
        if r.status_code == 200:
            for cookie in r.cookies:
                print(cookie)
    
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

#t = TOOLS() 
#t.getInput("https://adventofcode.com/2018/day/2/input")
#t.readCookie()