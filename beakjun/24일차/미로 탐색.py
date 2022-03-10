from collections import deque

N, M = map(int, input().split())
a = [list(map(str, input())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
q.append((0,0))
visit[0][0] = 1

while q:
    x, y = q.popleft()
    if x == N-1 and y == M-1:
        print(visit[x][y])
        break
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < M:
            if visit[nx][ny] == 0 and a[nx][ny] == '1':
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
