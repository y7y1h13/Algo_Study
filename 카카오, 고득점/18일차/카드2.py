from collections import deque


N = int(input())
q = deque()

for i in range(1, N + 1):
    q.append(i)
l = N
while l > 1:
    q.popleft()
    l -= 1
    q.append(q.popleft())
print(*q)