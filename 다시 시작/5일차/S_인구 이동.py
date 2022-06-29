from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    tmp = list()
    tmp.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if L <= abs(a[x][y] - a[nx][ny]) <= R:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                        tmp.append((nx, ny))
    return tmp


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    a = [list(map(int, input().split()))for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    round = 0
    while True:
        visited = [[0] * N for _ in range(N)]
        flag = False
        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    visited[r][c] = 1
                    cnt = bfs(r, c)
                    if len(cnt) > 1:
                        flag = True
                        n = sum([a[x][y] for x, y in cnt]) // len(cnt)
                        for x, y in cnt:
                            a[x][y] = n
        if not flag:
            break
        round += 1
    print(round)
