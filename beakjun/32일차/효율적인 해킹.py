from collections import deque


def bfs(x):
    k = 0
    q = deque()
    q.append(x)
    visited = [0] * (N + 1)
    visited[x] = 1
    while q:
        x = q.popleft()
        k += 1
        for i in a[x]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
    return k


N, M = map(int, input().split())
a = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    a[y].append(x)
tmp = 0
res = []
for i in range(1, N + 1):
    if a[i]:
        tmp2 = bfs(i)
        if tmp <= tmp2:
            if tmp < tmp2:
                res = []
            tmp = tmp2
            res.append(i)
print(*res)
