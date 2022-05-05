import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(x, y, cnt):
    global ans
    color[x][y] = cnt
    ans = max(ans, 1)
    for i in range(6):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < N:
            if a[nx][ny] == 'X':
                if color[nx][ny] == -1:
                    dfs(nx, ny, 1 - cnt)
                    ans = max(ans, 2)
                elif color[nx][ny] == cnt:
                    print(3)
                    exit()


N = int(input())
a = [list(input()) for _ in range(N)]
color = [[-1] * N for _ in range(N)]
dx = [-1, 0, 1, 1, 0, -1]
dy = [0, -1, -1, 0, 1, 1]
ans = 0
for i in range(N):
    for j in range(N):
        if a[i][j] == 'X' and color[i][j] == -1:
            dfs(i, j, 0)
print(ans)
