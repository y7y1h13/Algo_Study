import functools


def compare(a, b):
    t1 = a + b
    t2 = b + a
    if t1 > t2:
        return 1
    elif t1 < t2:
        return -1
    else:
        return 0


def solution(numbers):
    if not sum(numbers):
        return '0'
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=functools.cmp_to_key(compare), reverse=True)
    return ''.join(numbers)


print(solution([6, 10, 2]))
