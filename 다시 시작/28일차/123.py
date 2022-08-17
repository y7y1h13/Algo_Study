from collections import deque


def solution(X, Y):
    answer = ''
    tmp = list()
    if len(X) < len(Y):
        a = deque(sorted(list(X), reverse=True))
        b = deque(sorted(list(Y), reverse=True))
    else:
        a = deque(sorted(list(Y), reverse=True))
        b = deque(sorted(list(X), reverse=True))

    while a and b:
        k1 = a.popleft()
        k2 = b.popleft()
        if k1 == k2:
            tmp.append(k1)
        elif k1 > k2:
            b.appendleft(k2)
        else:
            a.appendleft(k1)
    print(tmp)

    return answer


print(solution("12321","42531"))