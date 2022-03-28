import copy
import sys


def sel_wall(srt, cnt):
    global m
    if cnt == 3:
        wall = copy.deepcopy(a)
        for x in range(N):
            for y in range(M):
                virus(x, y, wall)
        safe = sum(i.count(0) for i in wall)
        m = max(m, safe)
        return

    else:
        for i in range(srt, N * M):
            x = i // M
            y = i % M
            if a[x][y] == 0:
                a[x][y] = 1
                sel_wall(i, cnt + 1)
                a[x][y] = 0


def virus(x, y, wall):
    q = list()
    q.append([x, y])
    while q:
        x, y = q.pop()
        if wall[x][y] == 2:
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < N and 0 <= ny < M:
                    if wall[nx][ny] == 0:
                        wall[nx][ny] = 2
                        q.append([nx, ny])


if __name__ == "__main__":
    N, M = map(int, input().split())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    m = 0
    sel_wall(0, 0)
    print(m)
