from collections import deque


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a):
    start = []

    for i in range(5):
        for j in range(5):
            if a[i][j] == 'P':
                start.append((i, j))

    for s in start:
        q = deque()
        q.append((s[0], s[1], 0))
        visited = [[0] * 5 for _ in range(5)]
        visited[s[0]][s[1]] = 1

        while q:
            x, y, cnt = q.popleft()
            if cnt > 2:
                break
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < 5 and 0 <= ny < 5:
                    if not visited[nx][ny]:
                        if a[nx][ny] == 'O':
                            q.append((nx, ny, cnt + 1))
                            visited[nx][ny] = 1
                        if a[nx][ny] == 'P':
                            if cnt < 2:
                                return 0
    return 1


def solution(places):
    answer = []
    for i in places:
        answer.append(bfs(i))
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
