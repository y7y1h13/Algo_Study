def one():
    tmp = [[0] * M for _ in range(N)]
    for i in range(N):
        tmp[i] = a[N-1-i]
    return tmp


def two():
    tmp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            # tmp[i][M - 1 - j] = a[i][j]
            tmp[i][j] = a[i][M-1-j]
    return tmp


def three():
    tmp = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            # tmp[j][N - 1 - i] = a[i][j]
            tmp[i][j] = a[N-1-j][i]
    return tmp


def four():
    tmp = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            # tmp[M - 1 - j][i] = a[i][j]
            tmp[i][j] = a[j][M - 1 -i]
    return tmp


def five():
    tmp = [[0] * M for _ in range(N)]
    for i in range(N // 2):
        for j in range(M // 2):
            tmp[i][j + M // 2] = a[i][j]
    for i in range(N // 2):
        for j in range(M // 2, M):
            tmp[i + N // 2][j] = a[i][j]

    for i in range(N // 2, N):
        for j in range(M // 2, M):
            tmp[i][j - M // 2] = a[i][j]

    for i in range(N // 2, N):
        for j in range(M // 2):
            tmp[i - N // 2][j] = a[i][j]

    return tmp


def six():
    temp = [[0] * M for _ in range(N)]
    for i in range(N // 2):  # move position: 1 -> 4
        for j in range(M // 2):
            temp[i + N // 2][j] = a[i][j]

    for i in range(N // 2, N):  # move position: 4 -> 3
        for j in range(M // 2):
            temp[i][j + M // 2] = a[i][j]

    for i in range(N // 2, N):  # move position: 3 -> 2
        for j in range(M // 2, M):
            temp[i - N // 2][j] = a[i][j]

    for i in range(M // 2):  # move position: 2 -> 1
        for j in range(M // 2, M):
            temp[i][j - M // 2] = a[i][j]

    return temp


N, M, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
t = list(map(int, input().split()))

for i in t:
    if i == 1:
        a = one()
    elif i == 2:
        a = two()
    elif i == 3:
        a = three()
    elif i == 4:
        a = four()
    elif i == 5:
        a = five()
    else:
        a = six()

print(a)
