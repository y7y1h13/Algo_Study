N, M = map(int, input().split())
r, c, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = 1
cnt = 1

while True:
    flag = False
    for _ in range(4):
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        d = (d + 3) % 4
        if N > nx >= 0 == a[nx][ny] and 0 <= ny < M:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                flag = True
                break
    if not flag:
        if a[r - dx[d]][c - dy[d]]:
            print(cnt)
            break
        else:
            r, c = r - dx[d], c - dy[d]