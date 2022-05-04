import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)


def dfs(start, cnt, now):
    visited[now] = 0
    if start == now and cnt >= 2:
        check[start] = True
        return
    for i in a[now]:
        if visited[i]:

            dfs(start, cnt + 1, i)
        elif i == start and cnt >= 2:
            dfs(start, cnt, i)


def bfs():
    q = deque()
    for i in range(N):
        if check[i]:
            q.append(i)
            ans[i] = 0

    while q:
        now = q.popleft()
        for i in a[now]:
            if ans[i] == -1:
                q.append(i)
                ans[i] = ans[now] + 1


N = int(input())
a = {}

for i in range(N):
    a[i] = list()

for _ in range(N):
    i, j = map(int, input().split())
    a[i - 1].append(j - 1)
    a[j - 1].append(i - 1)
check = [False] * N
for start in range(N):
    visited = [1] * N
    dfs(start, 0, start)
ans = [-1] * N
bfs()
print(*ans)
