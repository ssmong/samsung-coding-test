"""백준 Python 입출력 템플릿.

PS에서 input()은 매우 느리다. 거의 항상 sys.stdin.readline 또는 일괄 read().
"""

import sys

# === 패턴 1: 한 줄씩 읽기 (가장 흔함) ===
input = sys.stdin.readline


def pattern_line_by_line():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    grid = [list(map(int, input().split())) for _ in range(N)]
    return N, M, arr, grid


# === 패턴 2: 전체 일괄 읽기 (입력이 매우 클 때) ===
def pattern_bulk_read():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    arr = [int(next(it)) for _ in range(N)]
    return N, M, arr


# === 패턴 3: 출력 일괄 처리 (출력이 많을 때) ===
def pattern_bulk_write(results):
    # print를 N번 호출하는 대신 한 번에 출력
    sys.stdout.write('\n'.join(map(str, results)) + '\n')


# === 재귀 깊이 풀기 (DFS 재귀 시 필수) ===
def setup_recursion():
    sys.setrecursionlimit(10**6)


# === 그리드 입력 — 공백 없이 붙어있는 경우 ===
def read_grid_no_space(N):
    """예: '01101' → [0, 1, 1, 0, 1]"""
    return [list(map(int, input().strip())) for _ in range(N)]
