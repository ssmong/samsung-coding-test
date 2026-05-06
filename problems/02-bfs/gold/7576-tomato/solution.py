import sys
from collections import deque

RIPE = 1
UNRIPE = 0
VACANT = -1

def bfs(grid, n, m):
    dist = [[-1] * m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == RIPE:
                dist[i][j] = 0
                q.append((i, j))
    
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < m and 0 <= ny < n:
                if dist[nx][ny] == -1 and grid[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist

def main():
    input = sys.stdin.readline

    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    dist = bfs(box, N, M)

    for i in range(N):
        for j in range(M):
            if dist[i][j] == UNRIPE:
                print("-1")
                break
    
    print(max(dist))