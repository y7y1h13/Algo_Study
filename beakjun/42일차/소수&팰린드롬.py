def p(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def isPalinDrome(n):
    length = len(n) // 2
    for i in range(length):
        if n[i] != n[-i - 1]:
            return False
    return True


N = int(input())
while True:
    if N == 1:
        pass
    elif isPalinDrome(str(N)) and p(N):
        break
    N += 1
print(N)
