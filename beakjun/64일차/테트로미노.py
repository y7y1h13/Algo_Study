def dfs(x, y, cnt, s):
    global res
    if s + max(max(*a)) * (4-cnt) <= res:
        return

    if cnt == 4:
        if res < s:
            res = s
        return

    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    if cnt == 2:
                        visited[nx][ny] = 1
                        dfs(x, y, cnt+1, s+a[nx][ny])
                        visited[nx][ny] = 0
                    visited[nx][ny] = 1
                    dfs(nx, ny, cnt+1, s+a[nx][ny])
                    visited[nx][ny] = 0


N, M = map(int, input().split())
a = [list(map(int, input().split()))for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, a[i][j])
        visited[i][j] = 0
print(res)
