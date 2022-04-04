# from collections import deque
# from sys import stdin
#
#
# N = int(stdin.readline())
# stack = deque()
# for i in range(N):
#     a = stdin.readline().split()
#     for j in a:
#         stack.extend(j)
#         while stack:
#             print(stack.pop(),end='')
#         print(end=' ')

N = int(input())
for i in range(N):
    a = input().split()
    for j in a:
        print(j[::-1], end=' ')