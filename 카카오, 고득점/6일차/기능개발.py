from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 0
    t = 0
    while len(progresses) > 0:
        if progresses[0] + t * speeds[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            t += 1
    answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
