'''
Stuff Learned
    - currentDTG = datetime.datetime.now()
    - timedelta(minutes=1) used to incriment datetime
    - parse library makes parsing much easier than using re... returns a dict like object with keys
    - The class guard had an observation list outside of the __init__ function and it was apparently the same 
    list for every instance of the class? Spent a lot of time learning this lesson
    - Thanks to github.com/wimglenn for parse class and showing order matters when adding minutes 
'''

import sys, os
from parse import parse
import operator
import datetime
from collections import Counter
from datetime import timedelta

class guard(object):

    def __init__(self, id):
        self.id = id
        self.sleep = 0
        self.obs = []
        self.minute = {minute: 0 for minute in range(60)}
        self.most_freq = 0

    def timecard(self, dtg, status):
        self.obs.append([dtg, status])
            
    def calc_time(self):
        sleep_start = None
        for i in self.obs:
            dtg, status = i
            if status == "t":
                continue
            elif status == "s":
                sleep_start = dtg
            elif status == "a":
                if sleep_start == None:
                    pass
                else:
                    t1 = sleep_start
                    while t1 < dtg:
                        self.minute[t1.minute] += 1
                        self.sleep += 1
                        t1 += timedelta(minutes=1)
                    t1 = None

    def mostfreq(self):
        self.most_freq = max(self.minute, key = lambda x: self.minute.get(x))
        return self.most_freq


def openInput(fname):
    # Read, Process, Strip, Sort Input
    obs = []
    proc = []
    guards = {}
    with open(os.path.join(sys.path[0], fname)) as f:
        content = f.readlines()
        proc = [x.strip() for x in content]
    f.close()
    return proc

def part1():
    g= "[{t:ti}] Guard #{id:d} begins shift"
    event = "[{t:ti}] {event}"
    obs = openInput("d4.txt")
    guards = {}
    gd = []

    for i in obs: 
        dtg = datetime.datetime.strptime(i.split(']')[0].strip('['), "%Y-%m-%d %H:%M")
        pg = parse(g, i)
        pe = parse(event, i)
        if "Guard" in pe['event']:
            if pg['id'] not in guards:
                guards[pg['id']] = guard(pg['id'])

    for i in obs:
        dtg = datetime.datetime.strptime(i.split(']')[0].strip('['), "%Y-%m-%d %H:%M")
        pg = parse(g, i)
        pe = parse(event, i)
        if "Guard" in pe['event']:
            cid = pg['id']
            status = 't'
        elif "falls asleep" in pe['event']:
            status = 's'
        elif "wakes up" in pe['event']:
            status = 'a'
        guards[cid].timecard(dtg, status)

    for i in guards:
        guards[i].calc_time()
        gd.append(
            [
            "#"+str(guards[i].id),
            sum(guards[i].minute.values()),
            max(guards[i].minute, key=lambda k: guards[i].minute[k]),
            int(guards[i].id)*max(guards[i].minute, key=lambda k: guards[i].minute[k])
            ]
            )

    for i in sorted(gd, key=lambda x: x[1], reverse = True):
        print(i)
    
    print("*"*60)
    return guards

def part2(g):
    s = []
    for i in g:
        print(g[i].id, max(g[i].minute.values()), g[i].id * max(g[i].minute.values()))
        ids = g[i].id
        maxmin = max(g[i].minute.values())
        t = ids*maxmin
        s.append([ids, maxmin, t])
    print("*"*60)
    print(max(s[1]))


g = part1()
part2(g)

