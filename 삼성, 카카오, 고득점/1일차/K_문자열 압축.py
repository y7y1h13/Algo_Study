def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        a = ''
        n = 1
        pre = s[:i]
        for j in range(i, len(s) * 2, i):
            now = s[j:j + i]
            if pre == now:
                n += 1
            elif pre != now:
                if n == 1:
                    a += pre
                else:
                    a += str(n) + pre
                n = 1
            pre = now
        answer = min(answer, len(a))
    return answer


print(solution("xababcdcdababcdcd"))
