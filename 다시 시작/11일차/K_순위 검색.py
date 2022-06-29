from bisect import bisect_left
from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []
    a = defaultdict(list)
    for i in info:
        ii = i.split()
        i_key = ii[:-1]
        i_value = int(ii[-1])

        for k in range(5):
            for c in combinations(i_key, k):
                tmp = ''.join(c)
                a[tmp].append(i_value)
    for k in a:
        a[k].sort()

    for q in query:
        qq = q.split()
        q_key = qq[:-1]
        q_value = int(qq[-1])

        while 'and' in q_key:
            q_key.remove('and')

        while '-' in q_key:
            q_key.remove('-')

        q_key = ''.join(q_key)

        if q_key in a:
            scores = a[q_key]

            if scores:
                e = bisect_left(scores, q_value)

                answer.append(len(scores) - e)
        else:
            answer.append(0)

    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
