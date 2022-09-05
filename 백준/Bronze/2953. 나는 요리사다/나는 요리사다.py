a = [list(map(int, input().split()))for _ in range(5)]
n, m = 0, 0
for i in range(5):
    s = sum(a[i])
    if s > m:
        n = i
        m = s
print(n + 1, m)