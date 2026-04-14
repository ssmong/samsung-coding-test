# 백준 Workbook 22734 — BFS / DFS

> 출처: https://www.acmicpc.net/workbook/view/22734
> 삼성 기출은 아니지만 BFS·DFS 기본기를 다지기에 좋은 48문제.
> 1152(삼성 기출)과 겹치는 6개(1260, 13460, 14502, 14503, 16236, 17142)는 이미 등록되어 있어 생략.

## 진행 상태 범례
- ⬜ 미시작 · 🟨 진행중 · ✅ 통과 · 🔁 복습필요

---

## 문제 목록 (42개 신규 등록)

### Silver (13개)
| 번호 | 제목 | 카테고리 | 티어 | 상태 |
|---:|---|---|---|:---:|
| 2178 | 미로 탐색 | 02-bfs | Silver 1 | ⬜ |
| 2667 | 단지번호붙이기 | 02-bfs (flood fill) | Silver 1 | ⬜ |
| 2468 | 안전 영역 | 02-bfs (flood fill + brute force) | Silver 1 | ⬜ |
| 5014 | 스타트링크 | 02-bfs (1D) | Silver 1 | ⬜ |
| 1697 | 숨바꼭질 | 02-bfs (1D) | Silver 1 | ⬜ |
| 2583 | 영역 구하기 | 02-bfs (flood fill) | Silver 1 | ⬜ |
| 1389 | 케빈 베이컨의 6단계 법칙 | 02-bfs (all-pairs) | Silver 1 | ⬜ |
| 1743 | 음식물 피하기 | 02-bfs (flood fill) | Silver 1 | ⬜ |
| 2644 | 촌수계산 | 02-bfs (tree) | Silver 2 | ⬜ |
| 11724 | 연결 요소의 개수 | 02-bfs (connected components) | Silver 2 | ⬜ |
| 11725 | 트리의 부모 찾기 | 02-bfs (tree) | Silver 2 | ⬜ |
| 18352 | 특정 거리의 도시 찾기 | 02-bfs | Silver 2 | ⬜ |
| 17086 | 아기 상어 2 | 02-bfs (multi-source) | Silver 2 | ⬜ |
| 10971 | 외판원 순회 2 | 03-dfs-backtracking (TSP) | Silver 2 | ⬜ |
| 2606 | 바이러스 | 02-bfs (connected components) | Silver 3 | ⬜ |

### Gold (28개)
| 번호 | 제목 | 카테고리 | 티어 | 상태 |
|---:|---|---|---|:---:|
| 1525 | 퍼즐 | 02-bfs (state encoding) | Gold 2 | ⬜ |
| 1600 | 말이 되고픈 원숭이 | 02-bfs (state BFS) | Gold 3 | ⬜ |
| 2146 | 다리 만들기 | 02-bfs (multi-step) | Gold 3 | ⬜ |
| 2206 | 벽 부수고 이동하기 | 02-bfs (state BFS) | Gold 3 | ⬜ |
| 1726 | 로봇 | 02-bfs (state BFS) | Gold 3 | ⬜ |
| 2234 | 성곽 | 02-bfs (bitmask) | Gold 3 | ⬜ |
| 12851 | 숨바꼭질 2 | 02-bfs | Gold 4 | ⬜ |
| 13913 | 숨바꼭질 4 | 02-bfs (경로 복원) | Gold 4 | ⬜ |
| 2665 | 미로만들기 | 02-bfs (0-1 BFS) | Gold 4 | ⬜ |
| 2573 | 빙산 | 02-bfs + 시뮬 | Gold 4 | ⬜ |
| 9019 | DSLR | 02-bfs | Gold 4 | ⬜ |
| 1987 | 알파벳 | 03-dfs-backtracking | Gold 4 | ⬜ |
| 1707 | 이분 그래프 | 02-bfs (bipartite) | Gold 4 | ⬜ |
| 2617 | 구슬 찾기 | 03-dfs-backtracking (topological) | Gold 4 | ⬜ |
| 17141 | 연구소 2 | 04-combined (백트래킹+multi-source BFS) | Gold 4 | ⬜ |
| 1976 | 여행 가자 | 02-bfs (union find) | Gold 4 | ⬜ |
| 13549 | 숨바꼭질 3 | 02-bfs (0-1 BFS) | Gold 5 | ⬜ |
| 7576 | 토마토 | 02-bfs (multi-source) | Gold 5 | ⬜ |
| 7569 | 토마토 (3D) | 02-bfs (multi-source) | Gold 5 | ⬜ |
| 9205 | 맥주 마시면서 걸어가기 | 02-bfs (union find) | Gold 5 | ⬜ |
| 10026 | 적록색약 | 02-bfs (flood fill) | Gold 5 | ⬜ |
| 17836 | 공주님을 구해라! | 02-bfs (state BFS) | Gold 5 | ⬜ |
| 2589 | 보물섬 | 02-bfs (brute force) | Gold 5 | ⬜ |
| 1068 | 트리 | 03-dfs-backtracking | Gold 5 | ⬜ |
| 13459 | 구슬 탈출 | 04-combined | Gold 1 | ⬜ |
| 15644 | 구슬 탈출 3 | 04-combined | Gold 1 | ⬜ |
| 15653 | 구슬 탈출 4 | 04-combined | Gold 1 | ⬜ |

### 생략 (1152와 중복)
1260 DFS와 BFS · 13460 구슬 탈출 2 · 14502 연구소 · 14503 로봇 청소기 · 16236 아기 상어 · 17142 연구소 3

---

## 추천 학습 순서

**1단계 — BFS 기본 (Silver)**
1697 숨바꼭질 → 2178 미로 탐색 → 2667 단지번호붙이기 → 2583 영역 구하기 → 2468 안전 영역

**2단계 — DFS/그래프 기본 (Silver)**
2606 바이러스 → 11724 연결 요소의 개수 → 11725 트리의 부모 찾기 → 2644 촌수계산 → 1743 음식물 피하기

**3단계 — 응용 탐색 (Silver)**
5014 스타트링크 → 18352 특정 거리의 도시 찾기 → 1389 케빈 베이컨 → 17086 아기 상어 2 → 10971 외판원 순회 2

**4단계 — multi-source & 3D BFS (Gold 5)**
7576 토마토 → 7569 토마토 3D → 10026 적록색약 → 2589 보물섬 → 1068 트리

**5단계 — 상태 BFS (Gold 4~3)**
12851 숨바꼭질 2 → 13549 숨바꼭질 3 → 13913 숨바꼭질 4 → 9019 DSLR → 2206 벽 부수고 이동하기 → 1600 말이 되고픈 원숭이

**6단계 — 고난도 응용 (Gold 4~2)**
2573 빙산 → 2146 다리 만들기 → 1987 알파벳 → 1726 로봇 → 2234 성곽 → 1707 이분 그래프 → 2617 구슬 찾기 → 1525 퍼즐

**7단계 — 구슬 탈출 시리즈 (Gold 1)**
13459 구슬 탈출 → (13460 구슬 탈출 2는 1152에서) → 15644 구슬 탈출 3 → 15653 구슬 탈출 4

**보조 — 삼성 스타일 연구소 (Gold 4)**
17141 연구소 2 (14502 연구소 푼 뒤에)
