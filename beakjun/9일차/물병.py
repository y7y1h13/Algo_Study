import sys


def check(n, k):
    result = 0
    while bin(n).count('1') > k:
        cnt = 0
        cnt += bin(n).count('1')
        n += 1
        result += 1
    return result


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    print(check(N, K))
