from collections import deque


def bfs(x):
    global ans
    visited[x] = 0
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        for i in range(1, 7):
            nx = x + i
            if 1 <= nx <= 100 and visited[nx]:
                if a[nx]:
                    nx = a[nx][0]
                if visited[nx]:
                    q.append(nx)
                    visited[nx] = 0
                    board[nx] = board[x] + 1


N, M = map(int, input().split())
board = [0] * 101
visited = [1] * 101
a = [[] for _ in range(101)]
ans = 0
for _ in range(N + M):
    u, v = map(int, input().split())
    a[u].append(v)
bfs(1)
print(board[100])