from collections import deque


def solution(rows, columns, queries):
    answer = []
    a = [[0] * columns for _ in range(rows)]
    cnt = 0
    for i in range(rows):
        for j in range(columns):
            cnt += 1
            a[i][j] = cnt
    for que in queries:
        q = deque()
        r1, c1, r2, c2 = que

        for i in range(c1 - 1, c2):
            q.append(a[r1 - 1][i])

        for i in range(r1, r2):
            q.append(a[i][c2 - 1])

        for i in range(c2 - 2, c1 - 2, -1):
            q.append(a[r2 - 1][i])

        for i in range(r2 - 2, r1 - 1, -1):
            q.append(a[i][c1 - 1])

        q.rotate(1)
        answer.append(min(q))

        for i in range(c1 - 1, c2):
            a[r1 - 1][i] = q.popleft()

        for i in range(r1, r2):
            a[i][c2 - 1] = q.popleft()

        for i in range(c2 - 2, c1 - 2, -1):
            a[r2 - 1][i] = q.popleft()

        for i in range(r2 - 2, r1 - 1, -1):
            a[i][c1 - 1] = q.popleft()

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
