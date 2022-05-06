import sys
input = sys.stdin.readline


def sol():
    n, k = map(int, input().split())
    dp = [1] + [0] * k
    for _ in range(n):
        c = int(input())
        for j in range(c, k + 1):
            if dp[j - c] == 0:
                continue
            dp[j] += dp[j - c]
    print(dp[-1])
sol()