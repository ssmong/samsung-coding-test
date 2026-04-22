import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# To avoid off-by-one mistake, we put -1 at index 0 as a dummy
cmd2dir = [-1, 0, 2, 3, 1]

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3


# Dice: index meaning
# 0=top, 1=bottom, 2=north, 3=south, 4=east, 5=west
dice = [0] * 6

def roll(dice, d):
    t, b, n, s, e, w = dice
    if d == EAST:
        dice[0], dice[4], dice[1], dice[5] = w, t, e, b
    elif d == WEST:
        dice[0], dice[5], dice[1], dice[4] = e, t, w, b
    elif d == NORTH:
        dice[0], dice[2], dice[1], dice[3] = s, t, n, b
    elif d == SOUTH:
        dice[0], dice[3], dice[1], dice[2] = n, t, s, b

out = []

for cmd in commands:
    d = cmd2dir[cmd]
    nx, ny = x + dr[d], y + dc[d]

    if not (0 <= nx < N and 0 <= ny < M):
        continue

    roll(dice, d)
    x, y = nx, ny
    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0
    
    out.append(dice[0])

sys.stdout.write('\n'.join(map(str, out)))