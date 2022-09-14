def pipe(x, y, location):
    global ans
    if x == n - 1 and y == n - 1:  # 도착
        ans += 1
        return
    if location == 0 or location == 2:  # 가로로 갈 수 있는 경우
        if y + 1 < n and board[x][y + 1] == 0:
            pipe(x, y + 1, 0)
    if location == 1 or location == 2:  # 세로로 갈 수 있는 경우
        if x + 1 < n and board[x + 1][y] == 0:
            pipe(x + 1, y, 1)
    if x + 1 < n and y + 1 < n:
        if board[x + 1][y + 1] == 0 and board[x + 1][y] == 0 and board[x][y + 1] == 0:  # 대각선
            pipe(x + 1, y + 1, 2)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
if board[n - 1][n - 1] == 1:
    print(0)
else:
    pipe(0, 1, 0)
    print(ans)
