for i in range(int(input())):
    N = int(input())
    dp = [0] * (N + 1)
    a = [list(map(int, input().split()))for _ in range(2)]
    for j in range(1, N):
        if j == 1:
            a[0][j] += a[1][j-1]
            a[1][j] += a[0][j-1]
        else:
            a[0][j] += max(a[1][j-1], a[1][j-2])
            a[1][j] += max(a[0][j-1], a[0][j-2])
    print(max(a[0][N-1],a[1][N-1]))