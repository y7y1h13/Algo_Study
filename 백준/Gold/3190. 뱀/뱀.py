from collections import deque


def loc(x, y):
    if 0 <= x < N and 0 <= y < N:  # 범위 안에 있으면
        if (x, y) in body:  # 몸이랑 닿으면
            print(time)
            exit()
        elif apple[x][y]:  # 사과 만남
            body.append((x, y))
            b_visited[x][y] = 1
            apple[x][y] = 0
        else:  # 사과 없음
            body.append((x, y))
            body.popleft()
    else:  # 벽 밖으로 나감
        print(time)
        exit()


N = int(input())
apple = [[0] * N for _ in range(N)]  # 사과 위치

for _ in range(int(input())):
    x, y = map(int, input().split())
    apple[x - 1][y - 1] = 1

rot = {}  # 돌아야할 방향이랑 초
for _ in range(int(input())):
    a, b = input().split()
    rot[int(a)] = b

b_visited = [[0] * N for _ in range(N)]  # 몸 위치
time = 1  # 초
body = deque()  # 몸 위치 queue
body.append((0, 0))
b_visited[0][0] = 1  # 몸 위치 체크
x, y = 0, 0
locate = 1  # 바라보는 방향

while True:
    # 한칸 움직이기(바라보고 있는 방향에 따라서)
    if locate % 4 == 0:
        x -= 1
        loc(x, y)

    elif locate % 4 == 1:
        y += 1
        loc(x, y)

    elif locate % 4 == 2:
        x += 1
        loc(x, y)

    elif locate % 4 == 3:
        y -= 1
        loc(x, y)

    if time in rot: # 회전
        if rot[time] == 'D':
            locate += 1
        else:
            if locate - 1 < 0:
                locate = 3
            else:
                locate -= 1

    time += 1
