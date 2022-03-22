N = int(input())
a = [0]
for _ in range(N):
    a.append(int(input()))
dp = [0] * (N+1)

if N == 1:
    print(a[1])
else:
    dp[1] = a[1]
    dp[2] = a[1] + a[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + a[i-1]+a[i], dp[i-2]+a[i])
    print(dp[N])