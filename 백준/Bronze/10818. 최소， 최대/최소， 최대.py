import sys

input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
min_num = a[0]
max_num = a[0]
for i in range(1, N):
    if min_num > a[i]:
        min_num = a[i]
    if max_num < a[i]:
        max_num = a[i]
print(min_num, max_num)