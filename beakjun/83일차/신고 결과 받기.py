def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    res = {}

    for i in id_list:
        if i not in res:
            res[i] = [0]

    for j in range(len(report)):
        n = report[j].split()
        res[n[0]].append(n[1])
        res[n[1]][0] += 1

    for i in res:
        tmp = 0
        for j in res[i][1:]:
            if res[j][0] >= k:
                tmp += 1
        answer.append(tmp)
        tmp = 0
    return answer


print(solution(
    ["muzi", "frodo", "apeach", "neo"],
    ["muzi frodo", "apeach frodo",
     "frodo neo", "muzi neo", "apeach muzi"], 2))
