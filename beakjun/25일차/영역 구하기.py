def solution(x, y):
    q = list()
    q.append((x, y))
    tmp = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if a[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    tmp += 1
    ans.append(tmp)


M, N, K = map(int, input().split())
a = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
ans = list()
for i in range(K):
    t = list(map(int, input().split()))
    for j in range(t[1], t[3]):
        for k in range(t[0], t[2]):
            a[j][k] += 1

for i in range(M):
    for j in range(N):
        if a[i][j] == 0 and visited[i][j] == 0:
            visited[i][j] = 1
            solution(i, j)
            cnt += 1
print(cnt)
print(*sorted(ans))
