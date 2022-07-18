from collections import deque


def shift(r, c, q, rc):
    for i in range(r):
        for j in range(c):
            q.append(rc[i][j])
    q.rotate(c)
    for i in range(r):
        for j in range(c):
            rc[i][j] = q.popleft()


def rotate(r, c, q, rc):
    for i in range(r):
        if i == 0:
            for j in range(c):
                q.append(rc[i][j])
        elif i == r - 1:
            for j in range(c - 1, -1, -1):
                q.append(rc[i][j])
        else:
            for j in range(c - 1, 0, -1):
                if j == 0 or j == c - 1:
                    q.append(rc[i][j])
    q.append(rc[1][0])
    q.rotate(1)
    for i in range(r):
        if i == 0:
            for j in range(c):
                rc[i][j] = q.popleft()
        elif i == r - 1:
            for j in range(c - 1, -1, -1):
                rc[i][j] = q.popleft()
        else:
            for j in range(c - 1, 0, -1):
                if j == 0 or j == r - 1:
                    rc[i][j] = q.popleft()
    rc[1][0] = q.popleft()


def solution(rc, operations):
    r = len(rc)
    c = len(rc[0])
    q = deque()
    for i in operations:
        if i == 'ShiftRow':
            shift(r, c, q, rc)

        elif i == 'Rotate':
            rotate(r, c, q, rc)
    return rc


print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
#
#
#
# from collections import deque
#
#
# def solution(rc, operations):
#     q = deque()
#     for i in operations:
#         if i == 'ShiftRow':
#             for i in range(len(rc)):
#                 for j in range(len(rc[i])):
#                     q.append(rc[i][j])
#             q.rotate(len(rc[i]))
#             for i in range(len(rc)):
#                 for j in range(len(rc[i])):
#                     rc[i][j] = q.popleft()
#         elif i == 'Rotate':
#             for i in range(len(rc)):
#                 if i == 0:
#                     for j in range(len(rc[i])):
#                         q.append(rc[i][j])
#                 elif i == len(rc) - 1:
#                     for j in range(len(rc[i]) - 1, -1, -1):
#                         q.append(rc[i][j])
#                 else:
#                     for j in range(len(rc[i]) - 1, 0, -1):
#                         if j == 0 or j == len(rc[i]) - 1:
#                             q.append(rc[i][j])
#             q.append(rc[1][0])
#             q.rotate(1)
#             for i in range(len(rc)):
#                 if i == 0:
#                     for j in range(len(rc[i])):
#                         rc[i][j] = q.popleft()
#                 elif i == len(rc) - 1:
#                     for j in range(len(rc[i]) - 1, -1, -1):
#                         rc[i][j] = q.popleft()
#                 else:
#                     for j in range(len(rc[i]) - 1, 0, -1):
#                         if j == 0 or j == len(rc[i]) - 1:
#                             rc[i][j] = q.popleft()
#             rc[1][0] = q.popleft()
#     return rc