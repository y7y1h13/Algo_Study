# from itertools import combinations
#
#
# def solution(logs):
#     answer = list()
#     a = dict()
#     nam = []
#     for i in logs:
#         name, number, score = i.split()
#         if name not in a:
#             nam.append(name)
#             a[name] = {number: score}
#         elif number not in a[name]:
#             a[name][number] = score
#         elif number in a[name]:
#             a[name][number] = score
#
#     for i in combinations(nam, 2):
#         flag = True
#         name1, name2 = a[i[0]], a[i[1]]
#         if len(name1) < 5 or len(name2) < 5:
#             continue
#
#         elif len(name1) == len(name2):
#             for number, score in name1.items():
#                 if not flag:
#                     break
#                 if number in name2:
#                     if name2[number] == score:
#                         continue
#                     else:
#                         flag = False
#                 else:
#                     flag = False
#             if flag:
#                 answer.append(i[0])
#                 answer.append(i[1])
#     if len(answer) == 0:
#         return None
#     return sorted(set(answer))
#
#
# print(solution(["1901 10 50", "1909 10 50"]))
from itertools import combinations

a = [i for i in range(500)]
cnt = 1
for i in combinations(a, 2):
    print(cnt)
    cnt += 1