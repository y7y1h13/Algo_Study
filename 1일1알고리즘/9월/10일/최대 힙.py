import heapq
import sys

input = sys.stdin.readline
a = list()
l = 0
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if l == 0:
            print(0)
        else:
            l -= 1
            print(heapq.heappop(a)[1])
    heapq.heappush(a, (-n, n))
    l += 1
