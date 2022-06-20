import sys

input = sys.stdin.readline


N, M = map(int, input().split())
ans = 0
a = set(input().strip() for _ in range(N))
b = list(input().strip() for _ in range(M))
for i in b:
    if i in a:
        ans += 1
print(ans)