from collections import deque
from sys import stdin

def push(x):
    stack.append(x)


def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())


def size():
    print(len(stack))


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


N = int(input())
stack = deque()
for i in range(N):
    a = stdin.readline().split()
    if "push" in a:
        push(a[1])
    elif "pop" in a:
        pop()
    elif "size" in a:
        size()
    elif "empty" in a:
        empty()
    else:
        top()
