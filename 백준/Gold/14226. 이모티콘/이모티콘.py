from collections import deque


def bfs(win, clip, time):
    q = deque()
    q.append([win, clip, time])
    while q:
        w, c, t = q.popleft()
        if w == S:
            print(t)
            break
        if visited[w][w]:
            visited[w][w] = False
            q.append([w, w, t+1])
        if w+c <= S and visited[w+c][c]:
            visited[w+c][c] = False
            q.append([w+c, c, t+1])
        if w-1 >= 0 and visited[w-1][c]:
            visited[w-1][c] = False
            q.append([w-1, c, t+1])


S = int(input())
visited = [[True] * 1001 for _ in range(1001)]
bfs(1, 0, 0)