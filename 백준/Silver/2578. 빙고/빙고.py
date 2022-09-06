def a(x):
    for i in range(5):
        if board[x][i] != 0:
            return False
    return True


def b(y):
    for i in range(5):
        if board[i][y] != 0:
            return False
    return True


def c():
    for i in range(5):
        if board[i][i] != 0:
            return False
    return True


def d():
    for i in range(5):
        if board[i][4 - i] != 0:
            return False
    return True


board = list()
tmp = dict()
for i in range(5):
    k = list(map(int, input().split()))
    for j in range(5):
        tmp[k[j]] = [i, j]
    board.append(k)
an = [list(map(int, input().split()))for _ in range(5)]
ans = 0
bingo = 0
for i in range(5):
    for j in an[i]:
        ans += 1
        x, y = tmp[j]
        board[x][y] = 0
        if a(x): bingo += 1
        if b(y): bingo += 1
        if x == y:
            if c(): bingo += 1
        if x + y == 4:
            if d(): bingo += 1
        if bingo > 2:
            print(ans)
            exit(0)
