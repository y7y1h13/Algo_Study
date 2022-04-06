# from collections import deque
#
# a = deque(list(input()))
# ans = [-1] * 26
# i = 0
# while a:
#     k = a.popleft()
#     if ans[ord(k) - ord('a')] == -1:
#         ans[ord(k) - ord('a')] = i
#     i += 1
# print(*ans)

a = input()
ans = [-1] * 26
for idx, k in enumerate(a):
    if ans[ord(k) - ord('a')] == -1:
        ans[ord(k) - ord('a')] = idx
print(*ans)