def solution(N, graph):
    visit = [[0] * N for _ in range(N)]
    queue = [[0, 0]]

    dx = [1, 0]
    dy = [0, 1]
    flag = False

    while queue:
        x, y = queue.pop(0)

        if graph[x][y] == -1:
            flag = True
            break

        jump = graph[x][y]

        for i in range(2):
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump

            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append([nx, ny])
    print('HaruHaru') if flag else print('Hing')


if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    solution(N, graph)
