N, M = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
a = []


def dfs():
    if len(a) == M:
        print(' '.join(map(str, a)))
        return
    for i in range(0, N):
        if t[i] not in a:
            a.append(t[i])
            dfs()
            a.pop()


dfs()
