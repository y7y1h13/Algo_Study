import sys
from itertools import combinations


input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
a.sort()
ans = set([i for i in range(1, N*max(a) + 2)])
for i in range(1, N+1):
    for j in combinations(a, i):
        if sum(j) in ans:
            ans.discard(sum(j))
print(min(ans))