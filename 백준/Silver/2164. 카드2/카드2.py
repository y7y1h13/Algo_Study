from collections import deque


N = int(input())
a = deque([i for i in range(1, N + 1)])
while N > 1:
    a.popleft()
    a.append(a.popleft())
    N -= 1
print(*a)