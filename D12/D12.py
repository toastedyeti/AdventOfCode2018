# u/foglander's solution
'''
Stuff Learned:
- eumerate() -- allows us to loop over something and have an automatic counter
- parse library.... that was so much easier than spending 45 minutes getting the re expression just right

Remaining Questions:
- Why is was adding "..." to each side of the current generation?  The total curr length increases by four each generation and printing
each curr makes the # seem to move across the line and return to the begining 
'''
import parse as pr

init = "#.#.#...#..##..###.##.#...#.##.#....#..#.#....##.#.##...###.#...#######.....##.###.####.#....#.#..##"

rules = {}
pattern = pr.compile("{} => {}")
ins = []

with open ('d12.txt') as f:
    ins = [l.strip() for l in f.readlines()]

for i in ins:
    rule = pattern.parse(i)
    rules[rule[0]] = rule[1]

def plantcounter(status): 
    diff = (len(status)-100)//2
    ctr = 0
    for i, c in enumerate(status):
        if c == '#':
            ctr += (i - diff)
    return ctr
    

def part1():
    curr = init
    prev_sum = plantcounter(init)
    diffs = []
    iters = 21
    for i in range(iters):
        if (i == 20):
            print("Part 1: ", str(plantcounter(curr)))
        curr = "...." + curr + "....."
        #print(curr)         
        #print(len(curr))
        next = ""
        for x in range(2, len(curr) - 2):
            sub = curr[x-2:x+3]
            next += rules[sub]
        curr = next
        currsum = plantcounter(curr)
        diff = currsum - prev_sum
        diffs.append(diff)
        if(len(diffs) > 100): 
            diffs.pop(0)
            prev_sum = currsum

    last100diff = sum(diffs) // len(diffs)

    total = (50000000000 - iters) * last100diff + plantcounter(curr) 

    print("Part 2: " + str(total))

part1()



