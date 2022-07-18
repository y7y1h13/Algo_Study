import heapq
from sys import stdin

input = stdin.readline


def solution():
    a = sorted([list(map(int, input().split()))for _ in range(int(input()))])
    r = [-1]
    for s, e in a:
        if s < r[0]:
            heapq.heappush(r, e)
        else:
            heapq.heapreplace(r, e)
    return len(r)


if __name__ == "__main__":
    print(solution())