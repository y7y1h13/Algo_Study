T = list(int(input())for _ in range(int(input())))
dp = [0, 1, 2, 4] + [0] * max(T)
for i in range(4, max(T) + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for i in T:
    print(dp[i])