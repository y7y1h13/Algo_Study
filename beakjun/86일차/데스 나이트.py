from collections import deque


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y, cnt))
    visited[x][y] = 0
    while q:
        x, y, cnt = q.popleft()
        if r2 == x and c2 == y:
            print(cnt)
            exit()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]:
                    visited[nx][ny] = 0
                    q.append((nx, ny, cnt + 1))


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[1] * N for _ in range(N)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
bfs(r1, c1, 0)
print(-1)