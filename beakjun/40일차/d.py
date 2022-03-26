def solution(rounds):
    answer = 0
    part = ['a', 'b', 'c', 'd']
    for rou in rounds:
        couple = [['k', 'k']]
        for i in range(len(rou)):
            if (i == 0 and rou[i] == 'a') or (i == 1 and rou[i] == 'b') or (i == 2 and rou[i] == 'c') or \
                    (i == 3 and rou[i] == 'd'):
                answer += 1
            else:
                if rou[i] == 'a':
                    if rou[0] == rou[i] and couple[0] != [rou[0], rou[i]]:
                        couple = [rou[0], rou[i]]
                    else:
                        answer += 1

                elif rou[i] == 'b':
                    if rou[1] == rou[i] and couple[0] != [rou[1], rou[i]]:
                        couple = [rou[1], rou[i]]
                    else:
                        answer += 1

                elif rou[i] == 'c':
                    if rou[2] == rou[i] and couple[0] != [rou[2], rou[i]]:
                        couple = [rou[2], rou[i]]
                    else:
                        answer += 1

                elif rou[i] == 'd':
                    if rou[3] == rou[i] and couple[0] != [rou[3], rou[i]]:
                        couple = [rou[3], rou[i]]
                    else:
                        answer += 1

    return answer


print(solution([["b", "a", "a", "d"], ["b", "c", "a", "c"], ["b", "a", "d", "c"]]))
