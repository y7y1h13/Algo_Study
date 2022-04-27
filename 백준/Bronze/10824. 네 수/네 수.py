from collections import deque

a = deque(input().split())
for i in range(2):
    n1 = a.popleft()
    n2 = a.popleft()
    a.append(n1 + n2)

print(int(a.pop()) + int(a.pop()))
