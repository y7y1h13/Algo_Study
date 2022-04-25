N, M = map(int, input().split())
a = []


def dfs():
    if len(a) == M:
        print(' '.join(map(str, a)))
        return
    for i in range(1, N + 1):
        if i not in a:
            a.append(i)
            dfs()
            a.pop()


dfs()
