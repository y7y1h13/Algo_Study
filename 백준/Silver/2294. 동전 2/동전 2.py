n, k = map(int, input().split())
a = list(int(input()) for _ in range(n))
dp = [10001] * (k + 1)
dp[0] = 0
for i in a:
    for j in range(i, k + 1):
        dp[j] = dp[j] if dp[j] < dp[j - i] + 1 else dp[j - i] + 1
if dp[j] > 10000:
    print(-1)
    exit()
print(dp[k])