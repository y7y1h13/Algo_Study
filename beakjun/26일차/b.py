def solution(width, height, diagonals):
    a = [[0] * (width + 1) for _ in range(height + 1)]

    q = list()
    q.append((0, 0, 0))
    answer = 0
    dx = [1, -1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 1, -1, -1, 1, -1, 1]
    while q:
        x, y, z = q.pop()
        a[x][y] = 1
        if x == width and y == height:
            break
        elif z == 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= height and 0 <= ny <= width:
                    if a[nx][ny] == 0:
                        a[nx][ny] = 1
                        answer += 1
        elif z == 0:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

    return answer


solution(2, 2, [[1, 1], [2, 2]])
