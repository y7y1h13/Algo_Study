import heapq
import sys

input = sys.stdin.readline
a = list()
l = 0
for _ in range(int(input())):
    n = int(input())
    if n != 0:
        heapq.heappush(a, (-n))
    else:
        try:
            print(-1 * heapq.heappop(a))
        except:
            print(0)
