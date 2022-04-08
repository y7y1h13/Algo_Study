def gcd(n1, n2):
    if n1 < n2:
        (n1, n2) = (n2, n1)
    while n2 != 0:
        (n1, n2) = (n2, n1 % n2)
    return n1


a, b = map(int, input().split())
print(gcd(a, b))
print(int(a * b / gcd(a, b)))
