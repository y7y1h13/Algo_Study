N = int(input())
a = list(map(int, input().split()))
tmp = 0
flag = True
if sum(a) % 3 == 0:
    for i in range(N):
        tmp += a[i] // 2
    if tmp < sum(a) // 3:
        flag = False
else:
    flag = False
print('YES') if flag else print('NO')