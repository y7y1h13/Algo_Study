def solution(N):
    result = 0
    for i in range(int(N/2), N+1):
        t = list(map(int, str(i)))
        result = i + sum(t)
        if result == N:
            print(i)
            break
        elif i == N:
            print(0)


if __name__ == '__main__':
    N = int(input())
    solution(N)