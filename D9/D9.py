from collections import deque, defaultdict
# understanding through u/marcusandrews solution
# 478 players; last marble is worth 71240 points
'''
Stuff Learned:
- Like last year if the problem is a circle, a deque is required!
- Deques are best understood as a circle that can be roated left & right as well as access from both ends of the queue
    - .appendleft()
    - .pop() / popleft()
'''

def part1(players, l_marble):
    scores = {}
    for i in range(players):
        scores[i] = 0
    board = deque([0])
    player = 0

    for marble in range(1, l_marble + 1):
        #print(board)
        if marble % 23 == 0:
            board.rotate(7) # right rotation // 
            scores[player] += marble + board.pop() #pop is a right pop / .popleft() would pop from other side of the q
            board.rotate(-1)
        else:
            board.rotate(-1) # left rotation // left-most value becomes right- most all others move -1 index position
            board.append(marble)
        player = (player + 1) % players
    return max(zip(scores.values(), scores.keys()))

#print(part1(478,71240))
#print(part1(478, 71240*100)) #100x larger is not 100% larger :)
#print(part1(9,25))