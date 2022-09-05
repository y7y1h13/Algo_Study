import sys

input = sys.stdin.readline
input()
a = list(map(int, input().split()))
min_num = a[0]
max_num = a[0]
for i in a:
    if min_num > i:
        min_num = i
    if max_num < i:
        max_num = i
print(min_num, max_num)