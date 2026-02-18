def solution(progresses, speeds):
    answer = []
    days = []
    now = 0
    idx = 0
    for i in range(len(progresses)):
        a, b = divmod(100-progresses[i],speeds[i])
        days.append(a + 1 if b != 0 else a)
    for day in days:
        if now == 0:
            now = day
            answer.append(1)
        elif now >= day:
            answer[idx] += 1
        else:
            now = day
            answer.append(1)
            idx += 1
    return answer