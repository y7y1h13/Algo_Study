def cnt(a, b):
    ans = 0
    while a != 0:
        a //= b
        ans += a
    return ans


n, m = map(int, input().split())

five = cnt(n, 5) - cnt(m, 5) - cnt(n-m, 5)
two = cnt(n, 2) - cnt(m, 2) - cnt(n-m, 2)
print(min(five, two))