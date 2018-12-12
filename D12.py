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

def part1():
    



