N, S, M = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][S] = 1
for i in range(1, N + 1):
    for j in range(M + 1):
        if dp[i - 1][j] == 1:
            if j+a[i - 1] <= M:
                dp[i][j + a[i - 1]] = 1
            if j - a[i - 1] >= 0:
                dp[i][j - a[i - 1]] = 1
for i in range(M, -1, -1):
    if dp[N][i] == 1:
        print(i)
        exit()
print(-1)