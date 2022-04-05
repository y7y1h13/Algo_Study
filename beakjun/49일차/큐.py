from collections import deque
from sys import stdin

q = deque()
for i in range(int(stdin.readline().strip())):
    a = stdin.readline().strip().split()
    if a[0] == 'push':
        q.append(a[1])

    elif a[0] == 'pop':
        print(-1 if len(q) == 0 else q.popleft())

    elif a[0] == 'size':
        print(len(q))

    elif a[0] == 'empty':
        print(1 if len(q) == 0 else 0)

    elif a[0] == 'front':
        print(-1 if len(q) == 0 else q[0])

    elif a[0] == 'back':
        print(-1 if len(q) == 0 else q[-1])
