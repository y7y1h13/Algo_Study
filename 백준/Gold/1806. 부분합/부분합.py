import sys

input = sys.stdin.readline


N, S = map(int, input().split())
a = list(map(int, input().split()))
s, e = 0, 0
ans = 1e5
n_s = 0
while s < N:
    if n_s >= S:
        if ans > e - s:
            ans = e - s
        n_s -= a[s]
        s += 1
    elif e == N:
        break
    else:
        n_s += a[e]
        e += 1
if ans == 1e5:
    print(0)
else:
    print(ans)