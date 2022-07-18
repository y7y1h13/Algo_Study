def solution(str1, str2):
    a1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    a2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]

    union = set(a1) | set(a2)
    inter = set(a1) & set(a2)
    if not len(union):
        return 65536

    s1 = sum([min(a1.count(i), a2.count(i)) for i in inter])
    s2 = sum([max(a1.count(i), a2.count(i)) for i in union])

    return int(s1 / s2 * 65536)


print(solution('FRANCE', 'french'))


# import math
# import re
#
#
# def solution(str1, str2):
#     p = re.compile('^[a-zA-Z]*$')
#     answer = 65536
#     a = list()
#     b = list()
#     for i in range(len(str1) - 1):
#         if p.match(str1[i:i + 2]):
#             a.append(str1[i:i + 2].lower())
#
#     for i in range(len(str2) - 1):
#         if p.match(str2[i:i + 2]):
#             b.append(str2[i:i + 2].lower())
#
#     a1 = a.copy()
#     union = a.copy()
#
#     for i in b:
#         union.append(i) if i not in a1 else a1.remove(i)
#
#     inter = []
#     for i in b:
#         if i in a:
#             inter.append(i)
#             a.remove(i)
#     if not len(inter) and not len(union):
#         pass
#     else:
#         answer = math.trunc(len(inter) / len(union) * 65536)
#     return answer