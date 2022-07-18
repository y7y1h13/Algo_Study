def solution(s):
    answer = []
    a = s[2:-2].split("},{")
    a = sorted(a, key=lambda x: len(x))
    for i in a:
        for j in i.split(','):
            if j not in answer:
                answer.append(j)

    return list(map(int, answer))


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
