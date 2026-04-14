import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r][c] = 1

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

time = 0
while True:
    time += 1

    snake.append