# BFS와 DFS — 그래프 탐색 기초

> 백준 1260을 풀기 전에 읽어야 할 개념 노트.

## 1. 그래프 표현

코딩테스트에서 그래프를 코드에 담는 두 가지 방식:

### 인접 리스트 (Adjacency List) — **권장**
```python
graph = [[] for _ in range(N + 1)]   # 1-indexed
graph[u].append(v)
graph[v].append(u)                    # 양방향이면
```
- 공간 O(V + E), 희소 그래프(간선 적음)에 유리. 삼성 코테는 거의 다 이쪽.

### 인접 행렬 (Adjacency Matrix)
```python
adj = [[False] * (N + 1) for _ in range(N + 1)]
adj[u][v] = adj[v][u] = True
```
- 공간 O(V²). N ≤ 500 정도일 때만 고려. 두 정점 연결 여부 확인이 O(1).

---

## 2. DFS (깊이 우선 탐색)

한 방향으로 끝까지 들어갔다가 막히면 되돌아온다. **재귀** 또는 **명시적 스택**으로 구현.

### 재귀 버전
```python
import sys
sys.setrecursionlimit(10**6)

visited = [False] * (N + 1)

def dfs(u):
    visited[u] = True
    # 방문 처리(출력, 카운트 등)
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
```

### 스택 버전 (재귀 깊이 위험할 때)
```python
def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
```

**주의:** 스택 버전은 재귀와 방문 순서가 다를 수 있다. "정점 번호가 작은 것부터" 같은 조건이 있다면 재귀 버전이 자연스럽다. 스택 버전은 인접 리스트를 **내림차순**으로 정렬해야 같은 순서가 나온다 (LIFO).

---

## 3. BFS (너비 우선 탐색)

가까운 것부터 차례대로. **큐**로 구현. 가중치 없는 그래프에서 **최단 거리**를 구할 때 필수.

```python
from collections import deque

def bfs(start):
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        # 방문 처리
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True       # ← popleft 시점이 아니라 enqueue 시점에!
                q.append(v)
```

**가장 흔한 버그:** `visited`를 `popleft`할 때 표시하면 같은 노드가 큐에 여러 번 들어가서 TLE 또는 오답.

---

## 4. 정점 번호가 작은 것부터 방문하려면

인접 리스트를 미리 정렬한다:
```python
for i in range(1, N + 1):
    graph[i].sort()
```
정렬 후 DFS는 자연스럽게 작은 번호부터 깊이 들어가고, BFS도 작은 번호부터 큐에 들어간다.

---

## 5. 격자(2D) 위 BFS/DFS

삼성 코테에서 가장 많이 나오는 형태. 그래프를 명시적으로 만들지 않고 **방향 벡터**로 이웃을 계산.

```python
dx = [-1, 1, 0, 0]   # 상 하 좌 우
dy = [0, 0, -1, 1]

for d in range(4):
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
        ...
```
8방향이면 dx, dy를 8개. 자세한 건 [templates/grid.py](../templates/grid.py).

---

## 6. 시간 복잡도

| 알고리즘 | 인접 리스트 | 인접 행렬 |
|---|---|---|
| BFS | O(V + E) | O(V²) |
| DFS | O(V + E) | O(V²) |

V = 정점 수, E = 간선 수.

---

## 7. 언제 BFS, 언제 DFS?

| 상황 | 선택 |
|---|---|
| 가중치 없는 최단 거리 | **BFS** |
| 모든 경로/조합 탐색, 백트래킹 | **DFS** |
| 사이클 탐지, 위상 정렬 | DFS |
| 동시에 퍼지는 시뮬레이션 (불, 바이러스) | BFS (멀티소스: 처음에 모든 시작점을 큐에 넣는다) |

---

## 8. 첫 문제

[문제로 가기 → problems/02-bfs/silver/1260-dfs-and-bfs/](../problems/02-bfs/silver/1260-dfs-and-bfs/problem.md)
