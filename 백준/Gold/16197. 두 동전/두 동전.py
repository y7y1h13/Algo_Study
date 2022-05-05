from collections import deque


def bfs(x, y, w, z, cnt):
    q = deque()
    q.append((x, y, w, z, cnt))

    while q:
        x1, y1, x2, y2, cnt = q.popleft()
        if cnt + 1 > 10:
            return -1
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if nx1 == nx2 and ny1 == ny2:
                continue
            elif 0 <= nx1 < N and 0 <= ny1 < M and 0 <= nx2 < N and 0 <= ny2 < M:
                if a[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if a[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                q.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < N and 0 <= ny1 < M:
                return cnt + 1
            elif 0 <= nx2 < N and 0 <= ny2 < M:
                return cnt + 1
            else:
                continue
    return -1


N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
xy = []
for i in range(N):
    for j in range(M):
        if a[i][j] == 'o':
            xy.append([i, j])
print(bfs(xy[0][0], xy[0][1], xy[1][0], xy[1][1], 0))
