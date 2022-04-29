from collections import deque


def bfs(now, time):
    q = deque()
    q.append([now, time])
    while q:
        n, t = q.popleft()
        if n == K:
            print(t)
            break
        for nx in (n * 2, n + 1, n - 1):
            if nx / 2 == n:
                if 0 <= nx <= 100000 and visited[nx]:
                    visited[nx] = 0
                    q.appendleft([nx, t])
            else:
                if 0 <= nx <= 100000 and visited[nx]:
                    visited[nx] = 0
                    q.append([nx, t + 1])


N, K = map(int, input().split())
visited = [1] * 100001
bfs(N, 0)
