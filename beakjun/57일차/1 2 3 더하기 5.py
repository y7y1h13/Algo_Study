a = list(int(input()) for _ in range(int(input())))
dp = list([0, 0, 0] for _ in range(max(a) + 1))
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
for i in range(4, max(a) + 1):
    dp[i][0] = dp[i - 1][1] % 1000000009 + dp[i - 1][2] % 1000000009
    dp[i][1] = dp[i - 2][0] % 1000000009 + dp[i - 2][2] % 1000000009
    dp[i][2] = dp[i - 3][0] % 1000000009 + dp[i - 3][1] % 1000000009

for i in a:
    print(sum(dp[i]) % 1000000009)
