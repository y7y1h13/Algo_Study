def candy_count():
    ans = 1
    for i in range(N):
        row_cnt = 1
        col_cnt = 1
        for j in range(1, N):
            if a[i][j] == a[i][j - 1]:
                row_cnt += 1
            else:
                row_cnt = 1
            if row_cnt > ans:
                ans = row_cnt

            if a[j][i] == a[j - 1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            if col_cnt > ans:
                ans = col_cnt
    return ans


N = int(input())
a = [list(input()) for _ in range(N)]
ans = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if j + 1 < N:
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
            cnt = candy_count()
            if cnt > ans:
                ans = cnt
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
        if i + 1 < N:
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
            cnt = candy_count()
            if cnt > ans:
                ans = cnt
            a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
print(ans)
