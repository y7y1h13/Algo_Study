t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    result = 0
    for i in range(2, n):
        c = a[i] - a[i - 2]
        result = max(c, result)
    print(result)