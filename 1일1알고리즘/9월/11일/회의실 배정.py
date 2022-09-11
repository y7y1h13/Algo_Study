import sys

input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split()))for _ in range(n)]
a.sort(key=lambda x: (x[1], x[0]))
prev, ans = 0, 0
for s, e in a:
    if s >= prev:
        ans += 1
        prev = e
print(ans)