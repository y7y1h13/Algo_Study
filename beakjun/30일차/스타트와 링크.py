from itertools import combinations
N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
tmp = [i for i in range(N)]
ans = 1000
for t1 in combinations(tmp, N//2):
    s, l = 0, 0
    t2 = list(set(tmp) - set(t1))
    for i in combinations(t1, 2):
        s += a[i[0]][i[1]] + a[i[1]][i[0]]
    for j in combinations(t2, 2):
        l += a[j[0]][j[1]] + a[j[1]][j[0]]
    ans = min(ans, abs(s - l))
print(ans)