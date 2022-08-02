import sys

input = sys.stdin.readline


def bi_sec(data, search, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if data[mid] == search:
        return 1
    elif data[mid] < search:
        return bi_sec(data, search, mid + 1, end)
    else:
        return bi_sec(data, search, start, mid - 1)


if __name__ == "__main__":
    N = int(input())
    a = sorted(list(map(int, input().split())))
    M = int(input())
    k = list(map(int, input().split()))

    for i in k:
        print(bi_sec(a, i, 0, N - 1), end=' ')
