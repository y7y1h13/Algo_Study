from collections import deque


def bfs(win, clip, time):
    q = deque()
    q.append([win, clip, time])
    while q:
        win, clip, time = q.popleft()
        if win == S:
            print(time)
            break
        if visited[win][win]:
            visited[win][win] = False
            q.append([win, win, time+1])
        if win+clip <= S and visited[win+clip][clip]:
            visited[win+clip][clip] = False
            q.append([win+clip, clip, time+1])
        if win-1 >= 0 and visited[win-1][clip]:
            visited[win-1][clip] = False
            q.append([win-1, clip, time+1])


S = int(input())
visited = [[True] * 1001 for _ in range(1001)]
bfs(1, 0, 0)