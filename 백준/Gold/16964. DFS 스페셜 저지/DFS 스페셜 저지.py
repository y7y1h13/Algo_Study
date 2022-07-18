def rank(a, eq):
    rnk = [-1 for i in range(N + 1)]
    for i in range(1, N + 1):
        rnk[eq[i - 1]] = i

    for i in range(1, N + 1):
        a[i] = sorted(a[i], key=lambda x: rnk[x], reverse=True)
    return a


def check(eq, ans):
    if ans == eq:
        print(1)
        exit()
    else:
        print(0)
        exit()


def dfs(a, eq):
    rank(a, eq)
    ans = []
    q = list()
    q.append(1)
    visited = [1] * (N + 1)
    visited[1] = 0

    while q:
        k = q.pop()
        ans.append(k)

        for i in a[k]:
            if visited[i]:
                visited[i] = 0
                q.append(i)
    check(eq, ans)


if __name__ == "__main__":
    N = int(input())
    a = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)
    eq = list(map(int, input().split()))
    dfs(a, eq)
