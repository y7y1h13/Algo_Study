import heapq
from sys import stdin

input = stdin.readline


def solution(N, a):
    a.sort()
    r = list()
    heapq.heappush(r, a[0][1])
    for i in range(1, N):
        if a[i][0] >= r[0]:
            heapq.heappop(r)
            heapq.heappush(r, a[i][1])
        else:
            heapq.heappush(r, a[i][1])
    return len(r)


if __name__ == "__main__":
    N = int(input())
    a = [list(map(int, input().split()))for _ in range(N)]
    print(solution(N, a))