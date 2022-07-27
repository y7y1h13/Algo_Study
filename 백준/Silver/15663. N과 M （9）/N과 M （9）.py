import sys
from itertools import permutations


input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    ans = set([i for i in permutations(a, M)])
    for i in sorted(ans):
        print(*i)


if __name__ == "__main__":
    solution()