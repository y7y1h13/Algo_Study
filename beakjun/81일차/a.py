def solution(survey, choices):
    score = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    m_score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(choices)):
        if choices[i] > 4:  # 뒤
            name = list(survey[i])[1]
            m_score[name] += score[choices[i]]

        elif choices[i] < 4:  # 앞
            name = list(survey[i])[0]
            m_score[name] += score[choices[i]]
    print(m_score)
    answer = ''
    for i in ['RT', 'CF', 'JM', 'AN']:
        name_1st = i[0]
        name_2nd = i[1]
        if m_score[name_1st] == m_score[name_2nd]:
            answer += min(name_1st, name_2nd)
        elif m_score[name_1st] > m_score[name_2nd]:
            answer += name_1st
        else:
            answer += name_2nd

    return answer


print(solution(["TR", "RT", "TR"], [7, 1, 3]))
