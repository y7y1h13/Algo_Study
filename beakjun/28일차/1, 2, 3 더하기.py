for _ in range(int(input())):
    n = int(input())
    a = [0, 1, 2, 4] + [0] * n
    for i in range(4, n + 1):
        a[i] = a[i-1] + a[i-2] + a[i-3]
    print(a[n])