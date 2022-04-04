from sys import stdin
N = int(stdin.readline())
tmp = []
for i in range(N):
    a = list(map(str, stdin.readline().strip()))
    if len(a) % 2 == 0:
        for j in range(len(a)):
            if a[-1] == ')':
                tmp.append(a.pop())
            elif len(tmp) > 0 and a[-1] == '(':
                tmp.pop()
                a.pop()
        if len(tmp) or len(a):
            print('NO')
        else:
            print('YES')
        tmp = []
    else:
        print('NO')