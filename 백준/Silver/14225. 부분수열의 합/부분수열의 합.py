import sys


input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(N):
    if i == 0:
        if a[i] == 1:
            continue
        else:
            print(1)
            break
    if sum(a[:i]) + 1 < a[i]:
        print(sum(a[:i]) + 1)
        break
else:
    print(sum(a, 1))