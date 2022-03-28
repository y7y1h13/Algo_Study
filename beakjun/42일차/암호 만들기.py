from itertools import combinations


def pw():
    global res

    for i in range(1, len(vow) + 1):
        if L - i == 1:
            break
        for v in combinations(vow, i):
            for c in combinations(cons, L - i):
                ans = list(v)
                ans.extend(list(c))
                res.append(''.join(sorted(ans)))
    return


if __name__ == "__main__":
    L, C = map(int, input().split())
    cons = list()  # 자음
    vow = list()  # 모음
    res = list()
    for i in input().split():
        if i in ['a', 'e', 'i', 'o', 'u']:
            vow.append(i)
        else:
            cons.append(i)
    pw()
    for i in (sorted(res)):
        print(i)
