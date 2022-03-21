def dfs(i, j, k):
    if len(k) == 6:
        ans.add(k)
        return
    if i < 0 or j < 0 or i > 4 or j > 4:
        return
    k += str(a[i][j])

    dfs(i, j + 1, k)
    dfs(i, j - 1, k)
    dfs(i + 1, j, k)
    dfs(i - 1, j, k)


a = [list(map(int, input().split())) for _ in range(5)]
ans = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, "")
print(len(ans))
