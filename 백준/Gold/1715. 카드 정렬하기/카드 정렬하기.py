import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = list(int(input()) for _ in range(n))
heapq.heapify(heap)
l, tmp, ans = 0, 0, 0
if n == 1:
    print(ans)
    exit(0)
while True:
    if len(heap) == 1:
        tmp += heapq.heappop(heap)
        ans += tmp
        print(ans)
        exit(0)
    else:
        if l == 1:
            tmp += heapq.heappop(heap)
            heapq.heappush(heap, tmp)
            ans += tmp
            l, tmp = 0, 0
        else:
            tmp = heapq.heappop(heap)
            l += 1