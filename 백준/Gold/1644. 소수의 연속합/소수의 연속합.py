import math


def isprime():
    prime_number = []
    array = [True for _ in range(N + 1)]

    for i in range(2, int(math.sqrt(N)) + 1):
        if array[i]:
            j = 2

            while i * j <= N:
                array[i * j] = False
                j += 1

    for num in range(2, N + 1):
        if array[num]:
            prime_number.append(num)

    return prime_number


def two_pointer():
    global ans
    s, e = 0, 0
    l = len(prime)
    s_n = 0
    while s < l:
        if s_n == N:
            s_n -= prime[s]
            s += 1
            ans += 1
        elif e == l:
            s_n -= prime[s]
            s += 1
        elif s_n > N:
            s_n -= prime[s]
            s += 1
        elif s_n < N:
            s_n += prime[e]
            e += 1


N = int(input())
ans = 0
prime = isprime()
two_pointer()
print(ans)
