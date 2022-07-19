import sys


input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    k = [0]
    s = 0
    for i in a:
        s += i
        k.append(s)

    for _ in range(M):
        s, e = map(int, input().split())
        print(k[e] - k[s - 1])


if __name__ == "__main__":
    solution()
