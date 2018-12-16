
puzzleInput = 540391
#540391

def part1(recipie):
    puzzin = int(recipie)
    recipies = [3,7]
    e1 = 0 
    e2 = 1
    
    for i in str(puzzin):
        recipies.append(int(i))

    while len(recipies) < puzzin + 10:
        new_formula = e1 + e2
        for digit in str(new_formula):
            recipies.append(int(digit))
        e1 = (e1 + 1 + recipies[e1]) % len(recipies)
        e2 = (e2 + 1 + recipies[e2]) % len(recipies)
    out = (''.join(str(num) for num in recipies)[puzzin:puzzin+10])
    print(out)

part1(puzzleInput)