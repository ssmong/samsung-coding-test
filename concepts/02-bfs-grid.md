---
trigger: 격자(2D) 위에서 최단 거리·동시 확산 시뮬레이션을 풀 때. 시작점이 여러 개면 멀티소스 BFS.
related_problems: [7576, 2178, 2667, 4179]
---

# 격자 BFS — 단일/멀티소스 템플릿

> [02-bfs-dfs.md](02-bfs-dfs.md)는 그래프 일반론. 이 노트는 **삼성 코테에서 90% 차지하는 격자 BFS**에 특화.
> 모든 코드는 명시적 파라미터 + `main()` 스타일.

## 언제 쓰나
- "최소 며칠/몇 칸 만에 도달?" → 가중치 없는 최단거리 = **BFS 확정**
- "동시에 퍼지는 불/바이러스/익음" → **멀티소스 BFS**
- DFS로도 도달 가능 여부는 풀리지만, **거리/시간**이 들어가면 BFS

## 코드 (멀티소스 + 거리 측정)

```python
import sys
from collections import deque
input = sys.stdin.readline

def bfs(grid, n, m):
    """grid에서 값이 1인 모든 칸을 시작점으로 BFS. dist 격자 반환."""
    dist = [[-1] * m for _ in range(n)]
    q = deque()

    # 1. 모든 시작점을 큐에 넣고 거리 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    # 2. BFS
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and grid[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return dist

def main():
    m, n = map(int, input().split())   # 백준 7576은 M N 순서!
    grid = [list(map(int, input().split())) for _ in range(n)]

    dist = bfs(grid, n, m)

    # 3. 답 추출: 빈칸(0)이 모두 채워졌는지 + 최대 거리
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and dist[i][j] == -1:
                print(-1); return
            if dist[i][j] > ans:
                ans = dist[i][j]
    print(ans)

main()
```

## 단일소스 BFS와의 차이

단일소스: 시작 좌표 1개를 큐에 넣고 시작.
멀티소스: **for 루프로 모든 시작점을 한 번에 큐에 넣는다.** 그 외 BFS 본문은 동일. "한 칸씩 펴진다"가 자동으로 동시 진행됨.

## 함정

- **방문 표시는 enqueue 시점에.** popleft 시점에 표시하면 같은 칸이 큐에 중복 들어가서 TLE 또는 거리 오염.
- **`dist == -1`로 미방문 체크.** `visited`와 `dist`를 따로 두면 동기화 실수가 생긴다. -1 sentinel 하나로 합치는 게 안전.
- **시작점이 0개일 수도 있다.** 7576에서 처음부터 모든 토마토가 익었으면(0이 없음) 답은 0. 빈칸 검사로 자동 처리됨.
- **벽 처리.** 벽 좌표는 큐에 넣지 않고 확장 조건(`grid[nx][ny] == 0`)에서 걸러낸다. 답 검사 시에도 빈칸만 본다.
- **N, M 순서.** 백준은 종종 `M N`을 입력으로 준다 (가로 세로). `range`와 인덱스에서 헷갈리지 말 것.
- **튜플 vs 리스트.** `dx, dy`는 `tuple`이 미세하게 빠르다. 핫 루프에선 의미 있을 수 있음.

## BFS 레벨 = 거리/시간

큐를 한 번 비우는 사이클이 "1단계 확산" = "하루". 별도 레벨 카운트 없이 `dist[x][y] + 1`로 자연스럽게 누적된다. 굳이 레벨별로 큐 사이즈 돌리며 `day += 1` 같은 패턴 쓰지 말 것 (불필요).

## 관련 개념
- [02-bfs-dfs.md](02-bfs-dfs.md) — 그래프 일반론
- [01-grid-template.md](01-grid-template.md) — 방향 벡터·경계 체크 관용구
- [00-mutable-reference.md](00-mutable-reference.md) — `[[-1]*m]*n` 같은 함정 주의
