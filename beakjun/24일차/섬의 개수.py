from collections import deque


def solution(i, j):
    q = deque()
    q.append((i, j))
    dx = [1, -1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 1, -1, -1, 1, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < h and 0 <= ny < w:
                if a[nx][ny] == 1:
                    q.append((nx, ny))
                    a[nx][ny] = 0


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    a = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == 1:
                a[i][j] = 0
                cnt += 1
                solution(i, j)
    print(cnt)
