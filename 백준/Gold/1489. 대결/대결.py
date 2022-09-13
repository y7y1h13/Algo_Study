# from collections import Counter
#
#
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.sort()
# b.sort(reverse=True)
# score = 0
# c_A = Counter(a)
# c_B = Counter(b)
# sort_A = sorted(c_A)
# sort_B = sorted(c_B, reverse=True)
#
# for i in sort_A:
#     for j in sort_B:
#         if i > j and c_A[i] and c_B[j]:
#             score += 2
#             c_A[i] -= 1
#             c_B[j] -= 1
#
# for i in sort_A:
#     for j in sort_B:
#         if i == j and c_A[i] and c_B[j]:
#             score += 1
#             c_A[i] -= 1
#             c_B[j] -= 1
# print(score)


N = int(input())
csortA = [0 for i in range(1002)]
csortB = [0 for i in range(1002)]

teamA = [int(x) for x in input().split()]
for i in range(N):
    csortA[teamA[i]] += 1
teamB = [int(x) for x in input().split()]
for i in range(N):
    csortB[teamB[i]] += 1

answer = 0

for i in range(1, 1001):
    while csortA[i]:
        tof = False
        for j in range(i - 1, 0, -1):
            if csortB[j]:
                tof = True
                answer += 2
                csortA[i] -= 1
                csortB[j] -= 1
                break
        if not tof:
            break
for i in range(1, 1001):
    while csortA[i] and csortB[i]:
        answer += 1
        csortA[i] -= 1
        csortB[i] -= 1

print(answer)