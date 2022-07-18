def fun(w, h):
    a, b = max([w, h]), min([w, h])
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


def solution(w, h):
    sq = w * h
    gcd = fun(w, h)
    return sq - (w + h - gcd)