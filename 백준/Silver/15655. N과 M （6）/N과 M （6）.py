N, M = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
a = []


def dfs(n):
    if len(a) == M:
        print(' '.join(map(str, a)))
        return
    for i in range(n, N):
        if t[i] not in a:
            a.append(t[i])
            dfs(i)
            a.pop()


dfs(0)
