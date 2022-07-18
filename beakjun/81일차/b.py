import sys
from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q = q1 + q2
    s_q = sum(q)
    max_res = sys.maxsize
    max_num = max(q)
    answer = 0
    if max_num <= (s_q - max_num) and s_q % 2 == 0:
        for i in range(max_res):
            if not len(q1) or not len(q2):
                return -1
            s_q1 = sum(q1)
            s_q2 = sum(q2)
            if s_q1 == s_q2:
                return answer
            elif s_q1 > s_q2:
                q2.append(q1.popleft())
            elif s_q1 < s_q2:
                q1.append(q2.popleft())
            answer += 1
    return -1


print(solution([3, 2, 7, 2]	, [4, 6, 5, 1]))
