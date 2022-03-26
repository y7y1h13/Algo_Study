def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    team_1, team_2, team_3 = dict(), dict(), dict()
    for num in range(len(employees)):
        for e in range(len(employees[num].split())):
            team = employees[num][0]
            if e == 0:
                if team == '1':
                    team_1[num] = True
                elif team == '2':
                    team_2[num] = True
                else:
                    team_3[num] = True
            else:
                if team == '1':
                    if employees[num].split()[e] in office_tasks:
                        team_1[num] = False
                elif team == '2':
                    if employees[num].split()[e] in office_tasks:
                        team_2[num] = False
                else:
                    if employees[num].split()[e] in office_tasks:
                        team_3[num] = False
    start = 0
    for i in (team_1, team_2, team_3):
        tmp = []
        flag = True
        for k in i:
            if k:
                tmp.append(k)
            else:
                flag = False
        if flag:
            tmp.pop(0)
        answer.extend(tmp)
    return answer


print(solution(3, ["development", "marketing", "hometask"], ["recruitment", "education", "officetask"],
         ["1 development hometask", "1 recruitment marketing", "2 hometask", "2 development marketing hometask",
          "3 marketing", "3 officetask", "3 development"]))
