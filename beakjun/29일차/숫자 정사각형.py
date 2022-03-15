N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
ans = 1
for i in range(N):
    for j in range(M):
        for k in range(ans, min(N, M)):
            if N <= i + k or M <= j + k:
                break
            if len(set([a[i][j], a[i+k][j], a[i][j+k], a[i+k][j+k]])) == 1:
                ans = max(ans, k+1)
print(ans ** 2)
