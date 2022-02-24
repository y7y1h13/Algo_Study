from itertools import combinations


def answer(M, a):
    result = 0
    for i in combinations(a, 3):
        if result < sum(i) <= M:
            result = sum(i)
    print(result)


if __name__ == '__main__':
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    answer(M, a)


# def answer(M, a):
#     result = 0
#     for i in range(N):
#         for j in range(i + 1, N):
#             for k in range(j + 1, N):
#                 if M >= a[i] + a[j] + a[k] > result:
#                     result = a[i] + a[j] + a[k]
#     print(result)
# if __name__ == '__main__':
# N, M = map(int, input().split())
#     a = list(map(int, input().split()))
#     answer(M, a)