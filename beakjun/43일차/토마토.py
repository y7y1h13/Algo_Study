from collections import deque


def solution():
    global ans
    q = deque(tomato)
    while q:
        x, y, day = q.popleft()
        if day > ans:
            ans = day
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if field[nx][ny] == 0:
                    field[nx][ny] = 1
                    q.append((nx, ny, day + 1))


if __name__ == "__main__":
    M, N = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    tomato = list()
    ans = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                tomato.append((i, j, 0))
    solution()
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                print(-1)
                exit(0)
    print(ans)
