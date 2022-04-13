from copy import deepcopy

N = int(input())
a = [0] + list(map(int, input().split()))
dp = deepcopy(a)
for i in range(1, N + 1):
    for k in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - k] + a[k])
print(dp[N])