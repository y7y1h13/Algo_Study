from collections import deque
from sys import stdin


N = int(stdin.readline().strip())
deq = deque()
for i in range(N):
    a = stdin.readline().strip().split()
    if a[0] == 'push_front':
        deq.appendleft(a[1])

    elif a[0] == "push_back":
        deq.append(a[1])

    elif a[0] == "pop_front":
        print(-1 if len(deq) == 0 else deq.popleft())

    elif a[0] == "pop_back":
        print(-1 if len(deq) == 0 else deq.pop())

    elif a[0] == "size":
        print(len(deq))

    elif a[0] == "empty":
        print(1 if len(deq) == 0 else 0)

    elif a[0] == "front":
        print(-1 if len(deq) == 0 else deq[0])

    else:
        print(-1 if len(deq) == 0 else deq[-1])
