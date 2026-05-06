# BFS와 DFS — 그래프 탐색 기초

> 백준 1260을 풀기 전에 읽어야 할 개념 노트.
> 모든 코드는 **명시적 파라미터** 스타일 (`bfs(graph, start, n)`). 이유는 [memory: feedback_explicit_params](../).

## 1. 그래프 표현

코딩테스트에서 그래프를 코드에 담는 두 가지 방식:

### 인접 리스트 (Adjacency List) — **권장**
```python
graph = [[] for _ in range(n + 1)]   # 1-indexed
graph[u].append(v)
graph[v].append(u)                    # 양방향이면
```
- 공간 O(V + E), 희소 그래프(간선 적음)에 유리. 삼성 코테는 거의 다 이쪽.

### 인접 행렬 (Adjacency Matrix)
```python
adj = [[False] * (n + 1) for _ in range(n + 1)]
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

def dfs(graph, u, visited):
    visited[u] = True
    # 방문 시 작업(출력, 카운트 등)
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, v, visited)

# 호출
visited = [False] * (n + 1)
dfs(graph, 1, visited)
```

> 깊은 재귀가 예상되면 인자를 줄이고 싶을 수 있음. 그땐 `visited`만 클로저/지역으로 캡처하는 inner 함수 패턴 사용. 격자 DFS처럼 깊이가 10⁶ 갈 수 있는 경우는 **BFS로 우회**가 더 안전.

### 스택 버전 (재귀 깊이 위험할 때)
```python
def dfs(graph, start, n):
    visited = [False] * (n + 1)
    stack = [start]
    visited[start] = True
    while stack:
        u = stack.pop()
        # 방문 시 작업
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return visited
```

**주의:** 스택 버전은 재귀와 방문 순서가 다를 수 있다. "정점 번호가 작은 것부터" 같은 조건이 있다면 재귀 버전이 자연스럽다. 스택 버전은 인접 리스트를 **내림차순**으로 정렬해야 같은 순서가 나온다 (LIFO).

---

## 3. BFS (너비 우선 탐색)

가까운 것부터 차례대로. **큐**로 구현. 가중치 없는 그래프에서 **최단 거리**를 구할 때 필수.

```python
from collections import deque

def bfs(graph, start, n):
    visited = [False] * (n + 1)
    visited[start] = True
    q = deque([start])
    while q:
        u = q.popleft()
        # 방문 시 작업 ← 문제별: 출력/카운트/합산 등. 비워둬도 BFS는 동작.
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True       # ← popleft 시점이 아니라 enqueue 시점에!
                q.append(v)
    return visited
```

**용어 구분:**
- **방문 표시** = `visited[v] = True` (이미 큐에 넣었다는 기록)
- **방문 시 작업** = `popleft` 직후 자리 (꺼낸 노드로 실제 작업 — 출력, 카운트, 거리 갱신 등)

**가장 흔한 버그:** `visited`를 `popleft`할 때 표시하면 같은 노드가 큐에 여러 번 들어간다 → 큐 폭발(TLE/MLE), 거리 BFS면 거리 오염. 룰: **"큐에 넣는 순간 표시. 꺼낼 때 아님."**

### 거리 측정 변형
`visited`를 `dist`로 합쳐서 한 배열로 처리:
```python
def bfs_dist(graph, start, n):
    dist = [-1] * (n + 1)        # -1 = 미방문
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
```

---

## 4. 정점 번호가 작은 것부터 방문하려면

인접 리스트를 미리 정렬한다:
```python
for i in range(1, n + 1):
    graph[i].sort()
```
정렬 후 DFS는 자연스럽게 작은 번호부터 깊이 들어가고, BFS도 작은 번호부터 큐에 들어간다.

---

## 5. 격자(2D) 위 BFS/DFS

삼성 코테에서 가장 많이 나오는 형태. 그래프를 명시적으로 만들지 않고 **방향 벡터**로 이웃을 계산. 자세한 템플릿은 [02-bfs-grid.md](02-bfs-grid.md) 참고.

```python
dx = (-1, 1, 0, 0)   # 상 하 좌 우
dy = (0, 0, -1, 1)

for d in range(4):
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
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
| 모든 경로/조합 탐색, 백트래킹 | **DFS** (재귀) |
| 사이클 탐지, 위상 정렬 | DFS |
| 동시에 퍼지는 시뮬레이션 (불, 바이러스) | BFS 멀티소스 |
| 격자에서 깊이가 큼 (N×M ≥ 10⁵) | BFS 우선, DFS면 스택 버전 |

---

## 8. 전체 main() 패턴

```python
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    dist = bfs(graph, 1, n)
    print(max(dist))

main()
```

이 패턴이 기본형. 모든 큰 데이터는 인자로 전달, 결과는 return. `n`도 인자로 (어차피 `len(graph)-1`로 구할 수도 있지만 가독성).

---

## 9. 첫 문제

[문제로 가기 → problems/02-bfs/silver/1260-dfs-and-bfs/](../problems/02-bfs/silver/1260-dfs-and-bfs/problem.md)
