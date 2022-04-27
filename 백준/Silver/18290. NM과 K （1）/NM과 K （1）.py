import math


def dfs(x, y):
    global ans
    if len(q) == K:
        tmp = 0
        for i in q:
            tmp += a[i[0]][i[1]]
        ans = max(ans, tmp)
        return
    for i in range(x, N):
        for j in range(y if i == x else 0, M):
            if [i, j] not in q:
                if ([i+1, j] not in q) and ([i-1, j] not in q) and ([i, j+1] not in q) and ([i, j-1] not in q):
                    q.append([i, j])
                    dfs(i, j)
                    q.pop()


N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
q = []
ans = -math.inf
dfs(0, 0)
print(ans)