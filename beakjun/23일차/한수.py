def solution(N):
    cnt = 0
    for i in range(1, N + 1):
        han = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif han[0] - han[1] == han[1] - han[2]:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    N = int(input())
    solution(N)
