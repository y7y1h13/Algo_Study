N = int(input())
dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N+1)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, N + 1):
    dp[i][0] = 1
    s = 1
    for j in range(1, 10):
        s += dp[i-1][j]
        dp[i][j] = s % 10007
print(sum(dp[N]) % 10007)