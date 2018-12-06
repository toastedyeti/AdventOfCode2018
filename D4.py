'''
Stuff Learned
    - currentDTG = datetime.datetime.now()
    - #s = sorted(s, key = lambda x: (x[1], x[2]))
    - #s = sorted(s, key = operator.itemgetter(1, 2))
'''

import AoCTools as tools
import re
import datetime
import operator
tool = tools.TOOLS()

puzzleInput = tool.openPuzzleInputTXT('d4s.txt')

class guard():
    def __init__(self, id):
        self.id = id
        self.sleepTime = 0
    

def part1(puzzleInput):
    guardTracker =[]
    guardSleep = {}
    currentGuard = ''
    lastDTG = ''

# read and strip input
    for i in puzzleInput:
        #Guard
        if re.findall(r"""\#\d+""",i):
            guard = re.findall(r"""\#\d+""",i)
        else:
            guard = ""
        #Shift
        if re.findall(r"""(begins)""", i):
            shift = shift = re.findall(r"""(begins)""", i)
        else:
            shift = ""
        #Sleep Status
        if re.findall(r"""(falls asleep)""",i):
            sleepStatus = "s"
        elif re.findall(r"""(wakes up)""",i):
            sleepStatus = "a"
        else:
            sleepStatus = ""
        date = re.findall(r"""\d+\-\d+\-\d+""",i)[0].split('-')
        time = re.findall(r"""\d+\:\d+""",i)[0].split(':')
        guardData = date + time + list(guard) + list(sleepStatus)
        guardTracker.append(guardData)

# create guard dictionary to store sleep times
    for i in guardTracker: #Create dictionary with guards
        if "#" in i[5]:
            if i[5] not in guardSleep:
                guardSleep[i[5]] = 0
        # Register First time
        if guardTracker.index(i) == 0:
            lastDTG = datetime.datetime(int(i[0]), int(i[1]), int(i[2]), int(i[3]), int(i[4]))

    for g in guardTracker:
        '''
            #datetime.datetime(year, month, date, hour, minute, second)
            0      1    2     3    4     5  
            y      m    d     h    m     guard / s / a
        '''
        currentDTG = datetime.datetime(int(g[0]), int(g[1]), int(g[2]), int(g[3]), int(g[4]))
        if '#' in g[5]:
            currentGuard = g[5]
        elif g[5] == 's':
            outTime = abs(currentDTG.minute - lastDTG.minute)
            guardSleep[currentGuard] += outTime
        lastDTG = currentDTG

    print(guardSleep)

    # track the minute the guard is most sleepy ... probably need a different tac 
part1(puzzleInput)

