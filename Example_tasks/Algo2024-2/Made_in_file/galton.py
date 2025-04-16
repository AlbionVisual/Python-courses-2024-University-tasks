import sys, random

n, trials = int(sys.argv[1]), int(sys.argv[2])

board = [0 for i in range(n)]

for i in range(trials):
    x = 0
    for j in range(n-1):
        r = random.randrange(2)
        x += r
        if (x > n - 1):
            x = n - 1
    
    board[x] += 1

print(board)