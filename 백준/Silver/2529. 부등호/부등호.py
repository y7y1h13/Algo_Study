def recu(idx):
    global MIN
    global MAX
    if idx == n+1:
        if MIN == 0:
            MIN = ''.join(map(str, s))
        else:
            MAX = ''.join(map(str, s))
        return

    for i in range(10):
        if i not in s:
            if len(s) == 0 or chk(s[-1], i, a[idx - 1]):
                s.append(i)
                recu(idx + 1)
                s.pop()


def chk(i, j, k):
    if k == '<':
        return i < j
    else:
        return i > j


n = int(input())
a = input().split()
MIN = 0
MAX = 0
s = []
recu(0)
print(MAX)
print(MIN)
