from itertools import combinations


def solution(relation):
    answer = 0
    r = len(relation)
    c = len(relation[0])
    candi = []
    for i in range(1, c + 1):
        candi.extend(combinations(range(c), i))

    uniq = []
    for cand in candi:
        tmp = [tuple([item[i] for i in cand]) for item in relation]
        if len(set(tmp)) == r:
            uniq.append(cand)
    answer = set(uniq)
    for i in range(len(uniq)):
        for j in range(i + 1, len(uniq)):
            if len(uniq[i]) == len(set(uniq[i]) & set(uniq[j])):
                answer.discard(uniq[j])

    return len(answer)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
