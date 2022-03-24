N = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(N)]
for i in range(N):
    t = a[i]
    cnt = 0
    for j in range(N):
        if cnt == t and b[j] == 0:
            b[j] = i + 1
            break
        elif b[j] == 0:
            cnt += 1
print(*b)
