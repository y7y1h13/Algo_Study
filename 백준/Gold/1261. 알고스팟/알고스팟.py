from collections import deque


def dfs(x, y):
    q = deque()
    q.append([0, 0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if ans[nx][ny] == -1:
                    if a[nx][ny] == 0:
                        ans[nx][ny] = ans[x][y]
                        q.appendleft([nx, ny])
                    else:
                        ans[nx][ny] = ans[x][y] + 1
                        q.append([nx, ny])


N, M = map(int, input().split())
a = [list(map(int, input()))for _ in range(M)]
ans = [[-1] * N for _ in range(M)]
ans[0][0] = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dfs(0, 0)
print(ans[M - 1][N - 1])