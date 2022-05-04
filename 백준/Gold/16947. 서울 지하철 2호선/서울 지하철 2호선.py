import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)


def make_graph(N):
    a = {}
    for i in range(N):
        a[i] = list()

    for _ in range(N):
        i, j = map(int, input().split())
        a[i - 1].append(j - 1)
        a[j - 1].append(i - 1)
    return a


def dfs(start, cnt, now):
    visited[now] = 0
    if start == now and cnt >= 2:
        ans[start] = 0
        return
    for i in graph[now]:
        if visited[i]:
            dfs(start, cnt + 1, i)
        elif i == start and cnt >= 2:
            ans[start] = 0
            return


def bfs():
    q = deque()
    for i in range(N):
        if not ans[i]:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if ans[i] == -1:
                q.append(i)
                ans[i] = ans[now] + 1


N = int(input())
graph = make_graph(N)
ans = [-1] * N


for start in range(N):
    visited = [1] * N
    dfs(start, 0, start)
bfs()
print(*ans)
