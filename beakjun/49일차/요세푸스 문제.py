from collections import deque
from sys import stdin


N, K = map(int, stdin.readline().strip().split())
q = deque(range(1, N + 1))
ans = []
while q:
    for i in range(1, K):
        q.append(q.popleft())
    ans.append(q.popleft())
print('<', end='')
print(*ans, sep=', ', end='')
print('>', end='')
