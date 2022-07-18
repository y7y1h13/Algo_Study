from collections import deque


def solution():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    robot = deque([0] * N)
    belt = deque(a)

    ans = 0
    while belt.count(0) < K:
        # 한 칸 회전
        belt.rotate(1)
        robot.rotate(1)

        # 로봇 내리기
        robot[N - 1] = 0

        # 로봇 이동
        for i in range(N - 2, 0, -1):
            if robot[i] and not robot[i + 1] and belt[i + 1]:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
            robot[-1] = 0

        # 첫 칸 체크
        if belt[0]:
            robot[0] = 1
            belt[0] -= 1
        ans += 1
    print(ans)


if __name__ == "__main__":
    solution()

