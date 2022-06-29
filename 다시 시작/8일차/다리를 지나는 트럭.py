from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    s = 0
    while bridge:

        tmp1 = bridge.popleft()
        if tmp1:
            s -= tmp1

        if trucks:
            tmp2 = trucks[0]
            if s + tmp2 <= weight:
                s += tmp2
                bridge.append(tmp2)
                trucks.popleft()
            else:
                bridge.append(0)
            answer += 1
    return answer + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))
