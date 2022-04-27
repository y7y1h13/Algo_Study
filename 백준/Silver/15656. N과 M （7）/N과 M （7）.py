def dfs():
    if len(q) == M:
        print(' '.join(map(str, q)))
        return

    for i in range(N):
        q.append(a[i])
        dfs()
        q.pop()


q = []
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
dfs()
