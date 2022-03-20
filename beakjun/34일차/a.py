import numpy as np


def one(a, s):
    r1 = s[1] - 1
    c1 = s[2] - 1
    r2 = s[3] - 1
    c2 = s[4] - 1
    cnt = 0
    for j in range(c1, c2 + 1):
        fst = a[r1][j]
        lst = a[r2][j]
        cnt += lst
        for i in range(r1, r2):
            tmp = a[i][j]
            if i == 0:
                a[i][j] = lst
            else:
                a[i][j] = tmp2
            tmp2 = tmp
        a[r2][j] = fst
    print(a)
    return a, cnt


def two(a, s):
    r1 = s[1] - 1
    c1 = s[2] - 1
    r2 = s[3] - 1
    c2 = s[4] - 1
    cnt = 0
    for j in range(c1, c2 + 1):
        fst = a[r2][j]
        lst = a[r1][j]
        cnt += lst
        for i in range(r2, r1, -1):
            tmp = a[i][j]
            if i == r2:
                a[i][j] = lst
            else:
                a[i][j] = tmp2
            tmp2 = tmp
        a[r1][j] = fst
    print(a)
    return a, cnt


def solution(rows, columns, swipes):
    answer = []
    a = (np.arange(rows * columns).reshape(rows, columns).tolist())

    for n in range(len(swipes)):
        if swipes[n][0] == 1:
            a, cnt = one(a, swipes[n])
            answer.append(cnt)
        elif swipes[n][0] == 2:
            a, cnt = two(a, swipes[n])
            answer.append(cnt)
        # elif swipes[n][0] == 3:
        #
        # else:

    return answer


print(solution(4, 3, [[1, 1, 2, 4, 3], [3, 2, 1, 2, 3], [4, 1, 1, 4, 3], [2, 2, 1, 3, 3]]))
