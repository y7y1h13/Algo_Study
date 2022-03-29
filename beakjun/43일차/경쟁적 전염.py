from collections import deque


def solution():
    q = deque(virus)
    while q:
        vir, x, y, time = q.popleft()
        if time == S:
            break
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N:
                if a[nx][ny] == 0:
                    a[nx][ny] = vir
                    q.append((vir, nx, ny, time + 1))
    return


if __name__ == "__main__":
    N, K = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split())
    virus = []
    for x in range(N):
        for y in range(N):
            if a[x][y] != 0:
                virus.append((a[x][y], x, y, 0))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    virus.sort()
    solution()
    print(a[X - 1][Y - 1])
