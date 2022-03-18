from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        t = q.popleft()

        for i in a[t]:
            if visited[i] == 0:
                visited[i] = visited[t] + 1
                q.append(i)


N, M = map(int, input().split())

a = [[] for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
ans = []

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    bfs(i)
    ans.append(sum(visited))

print(ans.index(min(ans)) + 1)
