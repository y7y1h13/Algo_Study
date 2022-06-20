import sys

input = sys.stdin.readline


N, M = map(int, input().split())
ans = 0
a = set(input().strip() for _ in range(N))

for _ in range(M):
    if input().strip() in a:
        ans += 1
print(ans)