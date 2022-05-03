def dfs(x, y, cnt):
    cnt += 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < M and a[nx][ny] == color:
            if [nx, ny] == start and cnt >= 4:
                print('Yes')
                exit()
            if visited[nx][ny]:
                visited[nx][ny] = 0
                dfs(nx, ny, cnt)


N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for x in range(N):
    for y in range(M):
        visited = [[1] * M for _ in range(N)]
        if visited[x][y]:
            visited[x][y] = 0
            start = [x, y]
            color = a[x][y]
            dfs(x, y, 0)
print('No')
