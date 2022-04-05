from collections import deque
from sys import stdin

S = list(stdin.readline().strip())
stack = []
q = deque()
res = ''
flag = True  # 괄호 안은 False 밖은 True
for i in S:
    if i == '<':
        while stack:
            res += stack.pop()
        q.append(i)
        flag = False
    elif i == '>':
        q.append(i)
        while q:
            res += q.popleft()
        flag = True

    elif i == ' ':
        if flag:
            while stack:
                res += stack.pop()
            res += ' '
        else:
            q.append(i)
            while q:
                res += q.popleft()

    else:
        if flag:
            stack.append(i)
        else:
            q.append(i)
while stack:
    res += stack.pop()
print(res)