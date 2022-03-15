from math import sqrt
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if dis == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == dis or r1 + r2 == dis:
        print(1)
    elif abs(r1 - r2) < dis < (r1 + r2):
        print(2)
    else:
        print(0)
        