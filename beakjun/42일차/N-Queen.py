def check(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[i] - board[x]) == abs(i - x):
            return False
    return True


def q(x):
    global ans
    if x == N:
        ans += 1
        return
    else:
        for i in range(N):
            board[x] = i
            if check(x):
                q(x + 1)


if __name__ == '__main__':
    N = int(input())
    ans = 0
    board = [0] * N
    q(0)
    print(ans)
