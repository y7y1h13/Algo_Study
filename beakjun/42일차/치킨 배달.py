from itertools import combinations
N, M = map(int, input().split())
city = [list(map(int, input().split()))for _ in range(N)]
chicken = list()
house = list()
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i, j])
        elif city[i][j] == 1:
            house.append([i, j])
res = float('inf')
for com in combinations(chicken, M):
    tmp = 0
    for h in house:
        # t = []
        # for i in com:
        #     t.append(abs(h[0] - i[0]) + abs(h[1] - i[1]))
        # tmp += min(t)
        tmp += min([abs(h[0] - i[0]) + abs(h[1] - i[1])for i in com])
        if res <= tmp:
            break
    if tmp < res:
        res = tmp
print(res)