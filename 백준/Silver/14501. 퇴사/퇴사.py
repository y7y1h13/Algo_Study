def dfs(day, tmp):
    global ans
    if day == N + 1:
        ans = max(ans, tmp)
        return
    dfs(day+1, tmp)
    if day + a[day][0] <= N + 1:
        dfs(day+a[day][0], tmp + a[day][1])


N = int(input())
a = [[0]] + [list(map(int, input().split()))for _ in range(N)]
ans = 0
dfs(1, 0)
print(ans)