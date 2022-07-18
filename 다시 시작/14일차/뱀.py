L = int(input())
N = int(input())
k = L * 2 + 1
a = [[L, L]]
head = [L, L, 1]
rot = [input().split() for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
h_cnt = 0
timer = 0
while True:
    nx = head[0] + dx[head[2]]
    ny = head[1] + dy[head[2]]
    if 0 <= nx < k and 0 <= ny < k and [nx, ny] not in a:
        head[0] = nx
        head[1] = ny
        a.append([nx, ny])
        cnt += 1
    else:
        print(cnt)
        exit()
    if h_cnt != -1:
        if timer == int(rot[h_cnt][0]):
            if rot[h_cnt][1] == 'R':
                head[2] = (head[2] + 1) % 4
            else:
                if head[2] - 1 < 0:
                    head[2] = 0
                else:
                    head[2] -= 1
            timer = 0
            if h_cnt == len(rot) - 1:
                h_cnt = -1
        else:
            timer += 1
