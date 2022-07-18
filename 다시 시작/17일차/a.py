def solution(A, K):
    tmp = sorted(A)
    s1 = 0
    e1 = K
    answer = 2e9

    while e1 <= len(A):
        s2 = 0
        e2 = len(A) - 1
        slice = sorted(A[s1:e1])

        for i in slice:
            if i == tmp[s2]:
                s2 += 1
            elif i == tmp[e2]:
                e2 -= 1

        n = abs(tmp[s2] - tmp[e2])

        if n == abs(tmp[-1] - tmp[-2]):
            return n

        answer = min(answer, n)
        s1 += 1
        e1 += 1

    return answer


print(solution([3, 5, 1, 3, 9, 8], 4))
