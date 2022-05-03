# import sys
# from itertools import combinations
#
#
# input = sys.stdin.readline
#
# N = int(input())
# a = list(map(int, input().split()))
# a.sort()
# ans = set([i for i in range(1, N*max(a) + 2)])
# for i in range(1, N+1):
#     for j in combinations(a, i):
#         if sum(j) in ans:
#             ans.discard(sum(j))
# print(min(ans))
#########################################
# N = int(input())
# a = list(map(int, input().split()))
# a.sort()
# ans = 1
#
# for i in a:
#     if ans < i:
#         break
#     ans += i
# print(ans)
#########################################
import sys


input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(N):
    if i == 0:
        if a[i] == 1:
            continue
        else:
            print(1)
            break
    if sum(a[:i]) + 1 < a[i]:
        print(sum(a[:i]) + 1)
        break
else:
    print(sum(a, 1))