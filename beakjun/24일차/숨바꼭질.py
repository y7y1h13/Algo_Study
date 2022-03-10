from collections import deque

N, K = map(int, input().split())
q = deque()
q.append(N)
MAX = 10 ** 5
visit = [0] * (MAX + 1)
while q:
    x = q.popleft()
    if x == K:
        print(visit[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= MAX and not visit[nx]:
            visit[nx] = visit[x] + 1
            q.append(nx)
