N, M, P = map(int, input().split())
if N == 0:
    print(1)
else:
    a = list(map(int, input().split()))
    if N == P and a[-1] >= M:
        print(-1)
    else:
        res = N + 1
        for i in range(N):
            if a[i] <= M:
                res = i + 1
                break
        print(res)