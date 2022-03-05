# def solution(N):
#     x = [0 for _ in range(N + 1)]
#
#     for i in range(2, N + 1):
#         x[i] = x[i-1] + 1
#         if i % 3 == 0:
#             x[i] = min(x[i], x[i // 3] + 1)
#         if i % 2 == 0:
#             x[i] = min(x[i], x[i // 2] + 1)
#     print(x[N])
def solution(N):
    x = {1: 0, 2: 1}
    for i in range(2, N + 1):
        x[i] = x[i-1] + 1
    if i % 3 == 0:
        x[i] = min(x[i], x[i // 3] + 1)
    if i % 2 == 0:
        x[i] = min(x[i], x[i // 2] + 1)
    print(x[N])


if __name__ == "__main__":
    solution(int(input()))
