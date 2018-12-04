import AoCTools as tools
import re
import datetime
import operator
tool = tools.TOOLS()

# year-month-day hour:minute
# Organize entries

#s = sorted(s, key = lambda x: (x[1], x[2]))
#s = sorted(s, key = operator.itemgetter(1, 2))


puzzleInput = tool.openPuzzleInputTXT('d4s.txt')

def part1(puzzleInput):
    guardTracker =[]
    guardSleep = {}
    currentGuard = ''
    lastDTG = None
    currentDTG = datetime.datetime.now()
    #datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
    
    for i in puzzleInput: #read and strip input
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

    for i in guardTracker: #Create dictionary with guards
        if "#" in i[5]:
            if i[5] not in guardSleep:
                guardSleep[i[5]] = 0

    for g in guardTracker:  #datetime.datetime(year, month, date, hour, minute, second)
        print(g)
        lastDTG = currentDTG
        currentDTG = datetime.datetime(int(g[0]), int(g[1]), int(g[2]), int(g[3]), int(g[4]))
        q = (currentDTG-lastDTG).seconds
        print(q, "?")


part1(puzzleInput)

