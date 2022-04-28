import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
M = int(input())
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for s in range(N - i):
        e = i + s
        if e == s:
            dp[s][e] = 1
        elif a[s] == a[e]:
            if s + 1 == e:
                dp[s][e] = 1
            elif dp[s + 1][e - 1] == 1:
                dp[s][e] = 1

for _ in range(M):
    start, end = map(int, input().split())
    print(dp[start - 1][end - 1])
