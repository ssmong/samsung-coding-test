import sys

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

DIRTY = 0
WALL = 1
CLEAN = 2

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d= map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

d -= 1 
d = d % 4

num_clean = 0

while True:

    if board[r][c] == DIRTY:
        board[r][c] = CLEAN
        num_clean += 1
    
    for i in range(4):
        d = (d - 1) % 4
        if board[r + dr[d]][c + dc[d]] == DIRTY:
            r += dr[d]
            c += dc[d]
            break
    else:
        br, bc = r - dr[d], c - dc[d]
        if board[br][bc] == WALL:
            break
        else:
            r = br
            c = bc

print(num_clean)

    