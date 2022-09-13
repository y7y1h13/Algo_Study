from collections import deque


def find(n, k):
    res = [0] * 5
    res[n] = k

    for i in range(n, 1, -1):  # 왼쪽 검사
        if a[i][6] == a[i - 1][2]:  # 같으면 회전 x
            break
        res[i - 1] = res[i] * -1

    for i in range(n, 4):  # 오른쪽 검사
        if a[i][2] == a[i + 1][6]:
            break
        res[i + 1] = res[i] * -1
    return res


a = {}
for i in range(1, 5):
    a[i] = deque(list(map(int, list(input()))))

for _ in range(int(input())):
    n, k = map(int, input().split())
    info = find(n, k)
    for i in range(1, 5):
        a[i].rotate(info[i])
ans = 0
if a[1][0] == 1:
    ans += 1
if a[2][0] == 1:
    ans += 2
if a[3][0] == 1:
    ans += 4
if a[4][0] == 1:
    ans += 8
print(ans)