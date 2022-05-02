N, M = map(int, input().split())
a = [list(map(int, input()))for _ in range(N)]
ans = 0

for i in range(1 << N * M):
    tmp = 0
    for row in range(N):
        r = 0
        for col in range(M):
            idx = row * M + col

            if i & (1 << idx) != 0:
                r = r * 10 + a[row][col]
            else:
                tmp += r
                r = 0
        tmp += r
    for col in range(M):
        c = 0
        for row in range(N):
            idx = row * M + col

            if i & (1 << idx) == 0:
                c = c * 10 + a[row][col]
            else:
                tmp += c
                c = 0
        tmp += c

    if ans < tmp:
        ans = tmp

print(ans)