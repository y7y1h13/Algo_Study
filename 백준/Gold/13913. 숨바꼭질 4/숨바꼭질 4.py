from collections import deque


def move(x):
    a = []
    t = x
    for _ in range(visited[x]+1):
        a.append(t)
        t = m[t]
    print(' '.join(map(str, a[::-1])))


def bfs(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            move(x)
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < 100001 and not visited[nx]:
                q.append(nx)
                visited[nx] = visited[x] + 1
                m[nx] = x


N, K = map(int, input().split())
visited = [0] * 100001
m = [0] * 100001
bfs(N)
