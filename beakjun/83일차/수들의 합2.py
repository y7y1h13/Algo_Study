N, M = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
s, e = 0, 0
while s < N:
    n_s = sum(a[s:e])
    if n_s == M:
        ans += 1
        s += 1
    elif e == N:
        s += 1
    elif n_s < M:
        e += 1
    else:
        s += 1
print(ans)