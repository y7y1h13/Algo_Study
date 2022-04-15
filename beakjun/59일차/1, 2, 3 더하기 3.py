a = list(int(input())for _ in range(int(input())))
dp = [0, 1, 2, 4] + [0] * max(a)

for i in range(4, max(a)+1):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009
for i in a:
    print(dp[i])