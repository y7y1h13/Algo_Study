import sys

input = sys.stdin.readline


N, S = map(int, input().split())
a = list(map(int, input().split()))
s, e = 0, 0
ans = 100000
n_s = 0
while s < N:
    if n_s >= S:
        if ans > e - s:
            ans = e - s
        n_s -= a[s]
        s += 1
    elif e == N:
        n_s -= a[s]
        s += 1
    elif n_s < S:
        n_s += a[e]
        e += 1
    else:
        n_s -= a[s]
        s += 1
if ans == 100000:
    print(0)
else:
    print(ans)