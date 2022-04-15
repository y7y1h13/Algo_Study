N = int(input())
a = list(map(int, input().split()))
dp = [1] * (N + 1)
for i in range(N):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

max_dp = max(dp)
max_idx = dp.index(max_dp)
l = list()

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        l.append(a[max_idx])
        max_dp -= 1
    max_idx -= 1
print(sum(l))
