def solution(money, costs):
    n = [1, 5, 10, 50, 100, 500]

    answer = 0
    t = 5
    while money != 0:
        total = []
        k = (money // n[t]) * n[t]
        if k != 0:
            for i in range(len(n) - 1, -1, -1):
                if (k // n[i]) * costs[i] != 0:
                    total.append((k // n[i]) * costs[i])
            print(total)
            answer += min(total)
            money %= n[t]
        t -= 1

    return answer


print(solution(4578, [1, 4, 99, 35, 50, 1000]))
