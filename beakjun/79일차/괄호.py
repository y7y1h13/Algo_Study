N = int(input())
a = list(int(input()) for _ in range(N))
dp = [0] * (max(a) + 1)
dp[0] = 1

for i in range(2, max(a) + 1, 2):
    for j in range(2, i + 1, 2):
        dp[i] += dp[j - 2] * dp[i - j]
    dp[i] %= 1000000007
for i in a:
    print(dp[i])