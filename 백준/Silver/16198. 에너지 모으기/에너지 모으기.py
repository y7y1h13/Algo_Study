def dfs(tmp):
    global ans
    if len(a) == 2:
        if ans < tmp:
            ans = tmp
        return
    for i in range(1, len(a) - 1):
        k = a[i]
        del a[i]
        dfs(tmp + a[i - 1] * a[i])
        a.insert(i, k)


N = int(input())
a = list(map(int, input().split()))
ans = 0
dfs(0)
print(ans)
