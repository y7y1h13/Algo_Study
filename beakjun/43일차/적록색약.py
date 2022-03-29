from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    color = a[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and a[nx][ny] == color:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


def dfs(x, y):
    q = list()
    q.append((x, y))
    visited[x][y] = 1
    color = a[x][y]
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and a[nx][ny] == color:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


if __name__ == "__main__":
    N = int(input())
    a = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ans = [0, 0]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                dfs(i, j)
                ans[0] += 1
    for i in range(N):
        for j in range(N):
            if a[i][j] == 'R':
                a[i][j] = 'G'
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                dfs(i, j)
                ans[1] += 1
    print(*ans)
