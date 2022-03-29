from collections import deque


def bfs():
    global ans

    q = deque(tomato)
    while q:
        x, y, z, day = q.popleft()
        if ans < day:
            ans = day
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if a[nz][nx][ny] == 0:
                    a[nz][nx][ny] = 1
                    q.append((nx, ny, nz, day + 1))


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    a = [[list(map(int, input().split())) for i in range(N)] for depth in range(H)]
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    ans = 0
    tomato = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if a[i][j][k] == 1:
                    tomato.append((j, k, i, 0))
    bfs()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if a[i][j][k] == 0:
                    print(-1)
                    exit(0)
    print(ans)
