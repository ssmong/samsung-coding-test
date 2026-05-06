import sys
from collections import deque

N = 0
S = 1
CW = 1
CCW = -1
NUM_GEAR = 4

U = 0
R = 2
L = 6

input = sys.stdin.readline

gears = [deque(map(int, input().strip())) for _ in range(NUM_GEAR)]

K = int(input())

queries = [tuple(map(int, input().split())) for _ in range(K)]

# Here, start should be 0-index
def rotate_all(gears, start_idx, direction):
    rot = [0] * NUM_GEAR
    rot[start_idx] = direction

    # Propagate to the right side
    for i in range(start_idx, NUM_GEAR-1):
        if gears[i][R] != gears[i+1][L]:
            rot[i+1] = -rot[i]
    
    for i in range(start_idx, 0, -1):
        if gears[i][L] != gears[i-1][R]:
            rot[i-1] = -rot[i]
    
    for i in range(NUM_GEAR):
        if rot[i]:
            gears[i].rotate(rot[i])


for gear_idx, dir in queries:
    rotate_all(gears, gear_idx-1, dir)

score_sum = 0
score = 1

for i in range(NUM_GEAR):
    if gears[i][U] == S:
        score_sum += score
    score *= 2

print(score_sum)