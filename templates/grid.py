"""격자(2D 배열) 위 시뮬레이션 템플릿.

삼성 코테에서 가장 자주 쓰이는 패턴들 모음.
"""

# === 방향 벡터 ===
# 4방향 (상 하 좌 우)
DX4 = [-1, 1, 0, 0]
DY4 = [0, 0, -1, 1]

# 8방향 (대각선 포함)
DX8 = [-1, -1, -1, 0, 0, 1, 1, 1]
DY8 = [-1, 0, 1, -1, 1, -1, 0, 1]


def neighbors4(x, y, N, M):
    """(x, y)의 4방향 이웃 중 격자 안에 있는 것만 yield."""
    for dx, dy in zip(DX4, DY4):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            yield nx, ny


def in_bounds(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


# === 2D 배열 90도 시계 회전 ===
def rotate_cw(grid):
    """N x M → M x N. 시계 방향 90도."""
    N, M = len(grid), len(grid[0])
    return [[grid[N - 1 - i][j] for i in range(N)] for j in range(M)]


def rotate_ccw(grid):
    """반시계 90도."""
    N, M = len(grid), len(grid[0])
    return [[grid[i][M - 1 - j] for i in range(N)] for j in range(M)]


# === 부분 영역 회전 (마법사 상어 류 문제) ===
def rotate_subgrid_cw(grid, r, c, size):
    """grid[r:r+size][c:c+size]를 in-place로 시계 회전."""
    sub = [[grid[r + i][c + j] for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            grid[r + j][c + size - 1 - i] = sub[i][j]


# === 격자 출력 (디버깅용) ===
def dump(grid):
    for row in grid:
        print(' '.join(f'{v:3}' for v in row))
    print()
