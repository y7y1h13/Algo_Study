from collections import deque


def solution(priorities, location):
    answer = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])

    while d:
        i = d.popleft()
        if d and max(d)[0] > i[0]:
            d.append(i)
        else:
            answer += 1
            if i[1] == location:
                break

    return answer


print(solution([2, 1, 3, 2], 2))

# from collections import deque
#
#
# def solution(priorities, location):
#     answer = 1
#     p = deque(priorities)
#     while p:
#         m = max(p)
#         if location == 0:
#             if p[0] >= m:
#                 return answer
#             else:
#                 p.append(p.popleft())
#
#         elif p[0] >= m:
#             p.popleft()
#             answer += 1
#         else:
#             p.append(p.popleft())
#         if location - 1 < 0:
#             location = len(p) - 1
#         else:
#             location -= 1
#
#     return answer