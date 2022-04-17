N = int(input())
a = list(map(int, input().split()))
b = a[::-1]
dp = [1] * (N)
dp2 = [1] * (N)
for i in range(N):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        if b[i] > b[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

print(max([i+j for i, j in zip(dp, dp2[::-1])]) - 1)