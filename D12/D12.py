# u/foglander's solution
'''
Stuff Learned:
- eumerate() -- allows us to loop over something and have an automatic counter
- parse library.... that was so much easier than spending 45 minutes getting the re expression just right
- Running Part1 for 50B iterations would have taken an extremely long time... Other solutions on reddit look for a stable solution, 
meaning 2 or more in diffs are the same indicating some predictable pattern.  This solution runs to 1000, averages the previous 100 diffs
and adds the current plant sum to the total answer.  
    * for x in range(generations):
        pots = "....pots...."
        diff = pots in pots
        if diff in diffs then stable

Remaining Questions:
- Why was it necessary to add "...." to front/back of each generation?  Is there a way to manage the movement
of the pots without adding additional characters?

'''
import parse as pr
from collections import defaultdict
import time
import os, sys

def setup():
    init = "#.#.#...#..##..###.##.#...#.##.#....#..#.#....##.#.##...###.#...#######.....##.###.####.#....#.#..##"
    pattern = pr.compile("{} => {}")
    rules = {}
    with open(os.path.join(sys.path[0], "d12.txt"), "r") as f:
        ins = [l.strip() for l in f.readlines()]
    f.close()

    for i in ins:
        rules[pattern.parse(i)[0]] = pattern.parse(i)[1]

    return rules, init

def plantc(curr):
    diff = (len(curr) - 100) // 2
    sum = 0
    for i, c in enumerate(curr):
        if c == '#':
            sum += (i - diff)
    return sum

def part1():
    rules, init = setup()
    current = init
    diffs  = []
    previous_sum = plantc(init)
    iters = 1000
    for i in range(iters):
        if i == 20:
            print("PART 1: ", str(plantc(current)))
            print(time.time() - t1)
        current = "...." + current + "...."
        next_ = ''
        for x in range(2, len(current)-2):
            sub = current[x-2:x+3]
            next_ += rules[sub]
        current = next_
        current_sum = plantc(current)
        diff = current_sum - previous_sum
        diffs.append(diff)
        if (len(diffs) > 100):
            diffs.pop(0)
        previous_sum = current_sum
    last100diff = sum(diffs) // len(diffs)
    total = (50000000000 - iters) * last100diff + plantc(current)
    print("PART 2: ", str(total))

t1 = time.time()
part1()

