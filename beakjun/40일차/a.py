def solution(logs):
    answer = 0
    log_name = ["team_name", "application_name", "error_level", "message"]
    for i in range(len(logs)):
        log_body = list()
        flag = True

        new_logs = logs[i].split()
        for log in new_logs:
            if log not in log_name:
                log_body.append(log)
        if len(logs[i]) <= 100 and len(log_body) == 8:
            for body in log_body:
                if len(body) <= 100 and ' ' not in body:
                    flag = False
                else:
                    flag = True

        if flag:
            answer += 1
    return answer


print(solution(["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"]))
