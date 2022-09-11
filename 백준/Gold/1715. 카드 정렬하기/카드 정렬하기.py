import heapq
import sys

input = sys.stdin.readline

heap = list(int(input()) for _ in range(int(input())))
heapq.heapify(heap)
ans = 0
while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a + b)
    ans += a + b
print(ans)