N, M = map(int, input().split())
a = []


def dfs(n):
    if len(a) == M:
        print(' '.join(map(str, a)))
        return
    for i in range(n, N + 1):
        if i not in a:
            a.append(i)
            dfs(i)
            a.pop()


dfs(1)
