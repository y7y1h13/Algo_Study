from collections import deque


def bfs(x, y):
    a[x][y] = 0
    w = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if a[nx][ny] == 1:
                    w += 1
                    a[nx][ny] = 0
                    q.append([nx, ny])
    return w

def dfs(x, y):
    a[x][y] = 0
    w = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = list()
    q.append([x, y])
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if a[nx][ny] == 1:
                    w += 1
                    a[nx][ny] = 0
                    q.append([nx, ny])
    return w

N, M, K = map(int, input().split())
a = [[0] * M for _ in range(N)]
for i in range(K):
    x, y = map(int ,input().split())
    a[x - 1][y - 1] = 1
cnt = 0

for i in range(N):
    for j in range(M):
        if a[i][j] == 1:
            cnt = max(cnt, bfs(i, j))
print(cnt)