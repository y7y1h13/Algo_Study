import sys
from collections import deque

input = sys.stdin.readline
def solution():
    q = deque()
    l = 0
    for i in range(int(input())):
        op = input().split()

        if len(op) == 2:
            q.append(int(op[1]))
            l += 1
        else:
            if op[0] == 'pop':
                if l:
                    print(q.popleft())
                    l -= 1
                else:
                    print(-1)

            elif op[0] == 'size':
                print(l)

            elif op[0] == 'empty':
                if l:
                    print(0)
                else:
                    print(1)

            elif op[0] == 'front':
                if l:
                    a = q.popleft()
                    print(a)
                    q.appendleft(a)
                else:
                    print(-1)
            else:
                if l:
                    a = q.pop()
                    print(a)
                    q.append(a)
                else:
                    print(-1)


solution()