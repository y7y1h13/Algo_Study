def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    while True:
        visited = [[0] * n for _ in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                k = board[i][j]
                if k != 0:
                    if board[i][j + 1] == k and board[i + 1][j] == k and board[i + 1][j + 1] == k:
                        visited[i][j], visited[i + 1][j], visited[i][j + 1], visited[i + 1][j + 1] = 1, 1, 1, 1

        cnt = 0
        for i in range(m):
            cnt += sum(visited[i])
        if not cnt:
            break
        answer += cnt
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if visited[i][j]:
                    x = i - 1
                    while x >= 0 and visited[x][j] == 1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        visited[x][j] = 1

    return answer


print(solution(8, 5, ["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"]))
