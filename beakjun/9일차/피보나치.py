def sol(n, fibo):
    answer = []
    if n == 0:
        return answer.append(0)
    for k in sorted(fibo, reverse=True):
        if k <= n:
            answer.append(k)
            n -= k
    return answer[::-1]


def get_fibo():
    fibo = [1, 2]
    while fibo[-1] <= 1000000000:
        fibo.append(fibo[-2] + fibo[-1])
    return fibo


if __name__ == '__main__':
    T = int(input())
    f = get_fibo()
    for i in range(T):
        result = sol(int(input()), f)
        print(*result)
