from collections import deque
from itertools import permutations
import copy


def operator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def cal(k, op):
    for o in op:
        s = deque()
        while k:
            tmp = k.popleft()
            if tmp == o:
                s.append(operator(s.pop(), k.popleft(), o))
            else:
                s.append(tmp)
        k = s
    return abs(k[0])


def solution(expression):
    result = 0
    op = ['*', '-', '+']
    a = list()
    n = ''
    for i in expression:
        if i in op:
            a.append(int(n))
            a.append(i)
            n = ''
        else:
            n += i

    a.append(int(n))

    a = deque(a)

    for i in permutations(op, 3):
        k = copy.deepcopy(a)
        result = max(result, cal(k, i))
    return result


print(solution("100-200*300-500+20"))
