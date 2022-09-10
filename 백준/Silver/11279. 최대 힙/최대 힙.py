import heapq
import sys

input = sys.stdin.readline
a = list()
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if len(a) == 0:
            print(0)
        else:
            print(heapq.heappop(a)[1])
    heapq.heappush(a, (-n, n))
