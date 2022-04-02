from itertools import combinations


def solution(dist):
    answer = []
    dic = dict()
    for i in combinations(range(5), 2):
        dic[dist[i[0]][i[1]]] = i
    dic = dict(sorted(dic.items(), reverse=True))
    tmp = [-1] * (max(dic) + 1)
    for idx, k in enumerate(dic.items()):
        if idx == 0:
            tmp[idx] = k[1][0]
            tmp[idx + k[0]] = k[1][1]
        elif k[1][0] in tmp and k[1][1] in tmp:
            continue
        elif k[1][0] in tmp:
            if (tmp.index(k[1][0])) + k[0] > len(tmp):
                tmp[(tmp.index(k[1][0])) - k[0]] = k[1][1]
            else:
                tmp[(tmp.index(k[1][0])) + k[0]] = k[1][1]
        else:
            if tmp.index(k[1][1]) + k[0] > len(tmp):
                tmp[(tmp.index(k[1][1])) - k[0]] = k[1][0]
            else:
                tmp[(tmp.index(k[1][1])) + k[0]] = k[1][0]

    tmp2 = [-1] * (max(dic) + 1)
    for idx, k in enumerate(dic.items()):
        if idx == 0:
            tmp2[idx] = k[1][1]
            tmp2[idx + k[0]] = k[1][0]
        elif k[1][0] in tmp2 and k[1][1] in tmp2:
            continue
        elif k[1][0] in tmp2:
            if (tmp2.index(k[1][0])) + k[0] > len(tmp2):
                tmp2[(tmp2.index(k[1][0])) - k[0]] = k[1][1]
            else:
                tmp2[(tmp2.index(k[1][0])) + k[0]] = k[1][1]
        else:
            if tmp2.index(k[1][1]) + k[0] > len(tmp2):
                tmp2[(tmp2.index(k[1][1])) - k[0]] = k[1][0]
            else:
                tmp2[(tmp2.index(k[1][1])) + k[0]] = k[1][0]
    ans = []
    for i in tmp:
        if i != -1:
            ans.append(i)
    answer.append(ans)
    ans2 = []
    for i in tmp2:
        if i != -1:
            ans2.append(i)
    answer.append(ans2)

    return answer


solution([[0, 5, 2, 4, 1], [5, 0, 3, 9, 6], [2, 3, 0, 6, 3], [4, 9, 6, 0, 3], [1, 6, 3, 3, 0]])
