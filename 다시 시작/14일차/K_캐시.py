# from collections import deque
#
#
# def solution(cacheSize, cities):
#     answer = 0
#     cache = deque(maxlen=cacheSize)
#     if not cacheSize:
#         return 5 * len(cities)
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             answer += 1
#         else:
#             cache.append(s)
#             answer += 5
#
#     return answer
#
#
# print(solution(2,
#                ["Jeju", "Pangyo", "NewYork", "newyork"]))


from collections import deque

q = deque(maxlen=3)
for i in range(4):
    q.appendleft(i)
print(q)