import sys

input = sys.stdin.readline
N = int(input())
a = sorted(list(map(int, input().split())))
s = 0
e = N - 1
tmp = 2e9
ans = list()
while s < e:
    tot = a[s] + a[e]
    if abs(tot) < tmp:
        tmp = abs(tot)
        ans = [a[s], a[e]]

    if tot < 0:
        s += 1
    else:
        e -= 1
print(*ans)