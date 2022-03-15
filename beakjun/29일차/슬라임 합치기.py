N = int(input())
a = sorted(list(map(int, input().split())))
tmp = 0
score = 0
for i in range(1, N):
    if i == 1:
        tmp = a[i-1] + a[i]
        score = a[i-1] * a[i]
    else:
        score += tmp * a[i]
        tmp += a[i]


print(score)
