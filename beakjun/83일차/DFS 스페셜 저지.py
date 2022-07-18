from collections import deque


def dfs():
    q = list()
    next = deque()
    q.append(1)
    visited = [1] * (N + 1)
    visited[1] = 0
    if eq[0] != 1:
        print(0)
        exit()

    while q:
        k = q.pop()
        for i in a[k]:
            if visited[i]:
                next.append(i)

        for _ in range(len(next)):
            n = eq.popleft()
            if n in next:
                q.append(n)
                visited[n] = 0
                break
            else:
                print(0)
                exit()

    print(1)


if __name__ == "__main__":
    N = int(input())
    a = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)
    eq = deque(list(map(int, input().split())))
    dfs()