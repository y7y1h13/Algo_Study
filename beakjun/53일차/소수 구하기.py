import math
k = 1000000
M, N = map(int, input().split())
a = [False, False] + [True] * 1000000
for i in range(2, int(math.sqrt(k+1))+1):
    if a[i]:
        for j in range(2*i, k+1, i):
            a[j] = False

for i in range(M, N+1):
    if a[i]:
        print(i)