import sys
from collections import deque

input = sys.stdin.readline


def answer():
    for i in range(x, x + w):
        q.append(a[y][i])

    for i in range(y + 1, y + h):
        q.append(a[i][x + w - 1])

    for i in range(x + w - 2, x, -1):
        q.append(a[y + h - 1][i])

    for i in range(y + h - 1, y, -1):
        q.append(a[i][x])

    q.rotate(-R)

    for i in range(x, x + w):
        a[y][i] = q.popleft()

    for i in range(y + 1, y + h):
        a[i][x + w - 1] = q.popleft()

    for i in range(x + w - 2, x, -1):
        a[y + h - 1][i] = q.popleft()

    for i in range(y + h - 1, y, -1):
        a[i][x] = q.popleft()


N, M, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
q = deque()
h = N
w = M
x, y = 0, 0
while True:
    if h == 0 or w == 0 : break
    answer()
    y += 1
    x += 1
    h -= 2
    w -= 2

for i in a:
    print(*i)
