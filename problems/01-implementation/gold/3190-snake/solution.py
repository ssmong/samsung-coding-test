import sys
from collections import deque

input = sys.stdin.readline

EMPTY = 0
APPLE = 1
SNAKE = 2

N = int(input())
K = int(input())

board = [[EMPTY] * (N+1) for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = APPLE

L = int(input())
turns = {}
for _ in range(L):
    x, c = input().split()
    turns[int(x)] = c

# Right / Down / Left / Up
dr = [0, 1, 0, -1]  
dc = [1, 0, -1, 0]
d = 0

snake = deque()
snake.append((1, 1))
board[1][1] = SNAKE

def in_range(r, c):
    return 1 <= r <= N and 1 <= c <= N

time = 0
while True:
    time += 1

    hr, hc = snake[-1]
    nr, nc = hr + dr[d], hc + dc[d]

    if not in_range(nr, nc):
        break

    if board[nr][nc] == SNAKE:
        break
    elif board[nr][nc] == APPLE:
        board[nr][nc] = SNAKE
        snake.append((nr, nc))
    else:
        board[nr][nc] = SNAKE
        snake.append((nr, nc))
        tr, tc = snake.popleft()
        board[tr][tc] = EMPTY

    if time in turns:
        if turns[time] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

print(time)        