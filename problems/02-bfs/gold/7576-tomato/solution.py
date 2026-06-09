import sys
from collections import deque

RIPE = 1
UNRIPE = 0
VACANT = -1

UNVISITED = -1

def bfs(grid, n, m):
    dist = [[UNVISITED] * m for _ in range(n)]
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
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == UNVISITED and grid[nx][ny] == UNRIPE:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist

def main():
    input = sys.stdin.readline

    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    dist = bfs(box, N, M)

    ans = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == UNRIPE and dist[i][j] == UNVISITED:
                print("-1"); return
            ans = max(ans, dist[i][j])
    
    print(ans)

if __name__ == "__main__":
    main()