def solution(N, M):
    p, k = list(), list()
    for i in range(M):
        a = input().split()
        p.append(int(a[0]))
        k.append(int(a[1]))
    p.sort()
    k.sort()
    ans = 0
    if p[0] <= k[0] * 6:
        if p[0] <= k[0] * (N % 6):
            ans += ((N // 6) + 1) * p[0]
        else:
            ans += (N // 6) * p[0]
            ans += (N % 6) * k[0]
    else:
        ans += k[0] * N

    print(ans)


if __name__ == "__main__":
    N, M = map(int, input().split())
    solution(N, M)
