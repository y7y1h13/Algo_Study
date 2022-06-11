def solution(record):
    answer = []
    name = {}
    for rec in record:
        k = rec.split()
        if k[0] in ['Enter', 'Change']:
            name[k[1]] = k[2]

    for i in record:
        k = i.split()
        if k[0] == 'Enter':
            answer.append(f"{name[k[1]]}님이 들어왔습니다.")
        elif k[0] == 'Leave':
            answer.append(f"{name[k[1]]}님이 나갔습니다.")
    return answer


print(solution(
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
