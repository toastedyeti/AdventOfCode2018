'''
#163 35
5705

Stuff Learned
    - currentDTG = datetime.datetime.now()
    - #s = sorted(s, key = lambda x: (x[1], x[2]))
    - #s = sorted(s, key = operator.itemgetter(1, 2))
'''
from collections import defaultdict
import re
import operator
import datetime

class guard(object):
    min_ctr = {str(i):0 for i in range(60)}

    def __init__(self, id):
        self.id = id
        self.sleep_stat = "a"
        self.sleep_tot = 0
        self.sleep_time = None

    def set_sleeptime(self, time):
        self.sleep_time = time
    
    def get_sleeptime(self):
        return self.sleep_time

    def update_min(self, minute):
        minute = str(minute.min)
        self.min_ctr[minute] += 1
    
    def set_status(self, status):
        self.status = status
    
    def get_status(self):
        return self.status

    def getID(self):
        return self.id
    
    def getMaxMinutes(self):
        #return max(zip(self.min_ctr.values(), self.min_ctr.keys()))
        #return max(self.min_ctr.keys())
        return(max(self.min_ctr, key=self.min_ctr.get))

    def add_sleep(self, mi):
        self.sleep_tot += mi

    def get_tot_sleep(self):
        return self.sleep_tot

def openInput(fname):
    # Read, Process, Strip, Sort Input
    p_out = []
    obs = []
    with open(fname) as f:
        content = f.readlines()
        p_out = [x.strip() for x in content]
    f.close()

    for i in p_out:
        #Guard
        if re.findall(r"""\#\d+""",i):
            guard = re.findall(r"""\#\d+""",i)
        else:
            guard = ""
        #Shift
        if re.findall(r"""(begins)""", i):
            shift = re.findall(r"""(begins)""", i)
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
        obs_ = date + time + list(guard) + list(sleepStatus)
        obs.append(obs_)
    
    return obs

def parse_dtg(l):
    y, m, d, h, mi = l[0:5]
    if re.match(r'0\d', mi):
        mi = int(mi[1])
    if re.match(r'00', h):
        h = int(h[1])
    return y,m,d,h,mi

def part1(obs):
    c_g = ''
    p_time = None
    p_date = None
    guards = {}
    # Generate Guards
    for i in obs:
        if '#' in i[5]:
            guards[i[5]] = guard(i[5])

    # Read Observation Lines
    for i in obs:
        # Generate Time
        y,m,d,h,mi = parse_dtg(i)
        c_date = datetime.date(int(y),int(m),int(d))
        c_time = datetime.time(int(h),int(mi))

        #Interpret Observations
        if '#' in i[5]:
            c_g = i[5]
            guards[c_g].set_status('a')
        elif i[5] == 's':
            guards[c_g].update_min(c_time.min)
            guards[c_g].set_sleeptime(c_time)
        elif i[5] == 'a':
            s_time = guards[c_g].get_sleeptime()
            s_time = s_time.min
            diff = c_time - s_time.min
            guards[c_g].add_sleep(t)
        
    # obs = observations
    # sleepiest = []
    # # Generate dict containing observed guards
    # # guards = {i[5]:guard(i[5]) if '#' in i[5] for i in obs}
    # guards = {} 
    # for i in obs:
    #     if '#' in i[5]:
    #         guards[i[5]] = guard(i[5])
    
    # c_g = None
    # p_time = None
    # p_date = None

    # for i in obs:
    #     timeDiff = 0

    #     # Set previous time as current if no val avail
    #     # if p_time == None and p_date == None:
    #     #     y,m,d,h,mi = parse_dtg(i)
    #     #     p_date = datetime.date(int(y),int(m),int(d))
    #     #     p_time = datetime.time(int(h),int(mi))
        
    #     #Set Current Time Variables
    #     y,m,d,h,mi = parse_dtg(i)
    #     c_date = datetime.date(int(y),int(m),int(d))
    #     c_time = datetime.time(int(h),int(mi))

    #     # Which guard is on duty? Set status to awake

    #     if i[5] == c_g:
    #         guards[c_g].set_status('')
    #         guards[c_g].update_min()
    #     else:
    #         c_g = guards[i[5]].getID()
    #         guards[c_g].set_status('a')

    #     else: # If no change to guard, status to a / s
    #         guards[c_g].set_status(i[5])
    #         if guards[c_g].get_status() == "s":
    #             guards[c_g].update_min(c_time.minute)
    #             if c_date.day > p_date.day:
    #                 h_delta = 60 - p_time.minute
    #                 min_delta = h_delta + c_time.minute
    #                 timeDiff = min_delta
    #                 guards[c_g].add_sleep(timeDiff)
    #             else:
    #                 timeDiff = c_time.minute - p_time.minute
    #                 guards[c_g].add_sleep(timeDiff)
    #         elif guards[c_g].get_status() == "a":
    #             pass
    #         else:
    #             pass
    #     #####
    #     p_time = c_time
    #     p_date = c_date
    
    # # Who was the sleepiest guard? What minute was the sleepiest?
    # # Return ID * Minute Chosen

    print(guards['#163'].min_ctr)
    print(guards['#163'].min_ctr['35'])

part1(openInput('d4s.txt'))