def solution(v, a, b):
    result = 0
    while True:
        if 0 in v:
            return result
        else:
            result += 1
            v[v.index(max(v))] -= (a - b)
            v - b


solution([4, 5, 5], 2, 1)