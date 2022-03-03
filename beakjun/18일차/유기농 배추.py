from collections import deque


def solution(M, N, i, j, visit):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    q.append([i,j])
    visit[i][j] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 1:
                visit[nx][ny] = 0
                q.append([nx, ny])


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        graph = [list(map(int, input().split())) for _ in range(K)]
        visit = [[0 for j in range(M)] for i in range(N)]
        for i, j in graph:
            visit[j][i] = 1
        cnt = 0
        for i in range(N):
            for j in range(M):
                if visit[i][j] == 1:
                    solution(M, N, i, j, visit)
                    cnt += 1
        print(cnt)
