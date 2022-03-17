N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = list()
for i in range(N):
    cnt = 0
    for j in range(N):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            cnt += 1
    ans.append(cnt + 1)
print(*ans)