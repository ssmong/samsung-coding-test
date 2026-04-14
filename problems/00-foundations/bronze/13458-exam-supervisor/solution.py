import sys

input = sys.stdin.readline

N = int(input())

list_A = list(map(int, input().split()))
B, C = map(int, input().split())

num_main = 0
num_main += N
num_sub = 0

for A in list_A:
    res_A = max(0, A - B)
    num_sub += (res_A + C - 1) // C

num_tot = num_main + num_sub
print(num_tot)