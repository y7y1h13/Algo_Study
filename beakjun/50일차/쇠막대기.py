# from collections import deque
#
# a = deque(list(input().replace('()', ' ')))
# cnt, ans = 0, 0
# while a:
#     i = a.popleft()
#     if i == ' ':
#         ans += cnt
#     elif i == '(':
#         cnt += 1
#     elif i == ')':
#         ans += 1
#         cnt -= 1
#
# print(ans)

a = list(input())
stack = []
ans = 0

for i in range(len(a)):
    if a[i] == '(':
        stack.append(1)

    else:
        stack.pop()
        if a[i-1] == '(':
            ans += len(stack)
        else:
            ans += 1
print(ans)