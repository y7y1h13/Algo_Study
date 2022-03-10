from collections import deque


def solution(n, x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N:
                if a[nx][ny] > n and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
min_a = min(map(min, a))
max_a = max(map(max, a))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = min_a
for i in range(min_a, max_a + 1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if a[j][k] > i and visited[j][k] == 0:
                solution(i, j, k)
                cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)
