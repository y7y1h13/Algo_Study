def dfs(cnt):
    flag = False
    print(cnt)
    if cnt == b_cnt:
        print('Puzzle', rotate)
        for r in range(9):
            print(*a[r], sep='')
        print()
        return True
    r, c = b[cnt]
    if a[r][c]:
        flag = dfs(cnt + 1)
        return flag
    for i in range(9):
        for j in range(9):
            if i == j or domi[i][j]:
                continue
            for k in range(2):
                nx = r + dx[i]
                ny = c + dy[i]
                if 0 <= nx < 9 and 0 <= ny < 9:
                    if not a[nx][ny]:
                        if r[r][i] == r[nx][j] == c[c][i] == c[ny][j] == \
                                s[r // 3 * 3 + c // 3][i] == s[nx // 3 * 3 + ny // 3][j] == 0:
                            a[r][c], a[nx][ny] = i + 1, j + 1
                            domi[i][j], domi[j][i] = 1, 1
                            r[r][i], r[nx][j], c[c][i], c[ny][j], s[r // 3 * 3 + c // 3][i], \
                            s[nx // 3 * 3 + ny // 3][j] = 1, 1, 1, 1, 1, 1
                            flag = dfs(cnt + 1)
                            if flag:
                                return flag
                            a[r][c], a[nx][ny] = 0, 0
                            domi[i][j], domi[j][i] = 0, 0
                            r[r][i], r[nx][j], c[c][i], c[ny][j], s[r // 3 * 3 + c // 3][i], \
                            s[nx // 3 * 3 + ny // 3][j] = 0, 0, 0, 0, 0, 0
    return flag


rotate = 1
while True:
    N = int(input())
    dx = [0, 1]
    dy = [1, 0]

    if N == 0:
        break

    a = [[0] * 9 for _ in range(9)]
    domi = [[1] * 9 for _ in range(9)]
    r = [[0] * 9 for _ in range(9)]
    c = [[0] * 9 for _ in range(9)]
    s = [[0] * 9 for _ in range(9)]
    b = []
    b_cnt = 0
    for _ in range(N):
        U, LU, V, LV = list(input().split())
        Ux, Uy = ord(LU[0]) - ord('A'), int(LU[1]) - 1
        Vx, Vy = ord(LV[0]) - ord('A'), int(LV[1]) - 1
        a[Ux][Uy], a[Vx][Vy] = int(U), int(V)
        domi[int(U) - 1][int(V) - 1], domi[int(V) - 1][int(U) - 1] = 1, 1
        r[Ux][int(U) - 1], r[Vx][int(V) - 1] = 1, 1
        c[Uy][int(U) - 1], c[Vy][int(V) - 1] = 1, 1
        s[Ux // 3 * 3 + Uy // 3][int(U) - 1] = 1
        s[Vx // 3 * 3 + Vy // 3][int(V) - 1] = 1
    for idx, k in enumerate(input().split()):
        kx, ky = ord(k[0]) - ord('A'), int(k[1]) - 1
        a[kx][ky] = idx + 1
        r[kx][idx], c[ky][idx] = 1, 1
        s[kx // 3 * 3 + ky // 3][idx] = 1
    for tx in range(9):
        for ty in range(9):
            if not a[tx][ty]:
                b.append([tx, ty])
                b_cnt += 1

    dfs(0)
    rotate += 1
