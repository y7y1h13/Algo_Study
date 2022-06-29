import sys


sys.stdin = open('sample_input.txt', 'r')


def solution():
    for r in range(int(input())):
        N = int(input())
        a = list(map(int, input().split()))
        round = 0
        eq = sorted(a)
        while True:
            if a == eq:
                break
            for i in range(0, len(a), 2):
                if i == len(a) - 1:
                    break
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]

            for j in range(1, len(a), 2):
                if j == len(a) - 1:
                    break
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
            round += 1
        print(f'#{r + 1} {round}')


if __name__ == "__main__":
    solution()
