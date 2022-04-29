T = int(input())
a = list(int(input()) for _ in range(T))
dp = [1] * (max(a) + 1)

for i in range(2, len(dp)):
    dp[i] += dp[i - 2]

for i in range(3, len(dp)):
    dp[i] += dp[i - 3]

for i in a:
    print(dp[i])