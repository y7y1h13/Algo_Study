def solution(clothes):
    answer = 0
    cloth = {}
    for c in clothes:
        if c[1] not in cloth:
            cloth[c[1]] = [c[0]]
        else:
            cloth[c[1]].append(c[0])

    for i in

    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
