N, K = map(int, input().split())

cnt = 0

a = [True] * (N + 1)
for i in range(2, len(a) + 1):
    for j in range(i, N + 1, i):
        if a[j] == True:
            a[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                break