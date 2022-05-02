from itertools import combinations as c
N, S = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    for j in c(a, i):
        if sum(j) == S:
            cnt += 1
print(cnt)