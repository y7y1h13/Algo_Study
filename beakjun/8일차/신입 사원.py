import sys
for _ in range(int(input())):
    cnt = 1
    a = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(int(input()))])
    m = a[0][1]
    for i in a:
        if m > i[1]:
            cnt += 1
            m = i[1]
    print(cnt)