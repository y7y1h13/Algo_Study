from collections import deque


def bfs(x, y, tmp):
    visited[x][y] = False
    q = deque()
    q.append([x, y, tmp])
    while q:
        x, y, tmp = q.popleft()
        if [x, y] == goal:
            global ans
            if ans > tmp:
                ans = tmp
                break
        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny]:
                    visited[nx][ny] = False
                    q.append([nx, ny, tmp+1])


l = int(input())
dxy = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
for _ in range(l):
    n = int(input())
    now = list(map(int, input().split()))
    goal = list(map(int, input().split()))
    a = [[0] * n for _ in range(n)]
    visited = [[True] * n for _ in range(n)]
    ans = 300
    bfs(now[0], now[1], 0)
    print(ans)