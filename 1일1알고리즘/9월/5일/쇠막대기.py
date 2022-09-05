import sys

input = sys.stdin.readline().rstrip
a = list(input())
s = []
ans = 0
for i in range(len(a)):
    if a[i] == '(':
        s.append(a[i])
    elif a[i - 1] == '(':
        s.pop()
        ans += len(s)
    else:
        ans += 1
        s.pop()
print(ans)