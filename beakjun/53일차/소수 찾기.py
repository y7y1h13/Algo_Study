from math import sqrt


def isprime(x):
    if x == 1:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    if isprime(i):
        ans += 1

print(ans)
