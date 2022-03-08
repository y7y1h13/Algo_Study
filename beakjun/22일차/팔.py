def solution(L, R):
    L = list(map(str, L))
    R = list(map(str, R))
    cnt = 0

    if len(L) != len(R) or L[0] != R[0]:
        print(0)
        exit(0)
    elif L[0] == '8':
        cnt += 1
    for i in range(1, len(L)):
        if L[i] != R[i]:
            break
        elif L[i] == '8':
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    L, R = input().split()
    solution(L, R)
