def dfs(num):
    if len(q) == M:
        print(' '.join(map(str, q)))
        return

    for i in range(num, N):
        q.append(a[i])
        dfs(i)
        q.pop()


q = []
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
dfs(0)
