from itertools import combinations


def solution(a):
    for i in combinations(a, 2):
        if sum(a) - sum(i) == 100:
            a.remove(i[0])
            a.remove(i[1])
            break
    for i in sorted(a):
        print(i)


if __name__ == '__main__':
    a = list(int(input()) for _ in range(9))
    solution(a)
