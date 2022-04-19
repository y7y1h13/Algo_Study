N = list(map(int, input().split()))
a = [1, 1, 1]
ans = 1
while True:
    if a == N:
        break
    a[0] = 1 if a[0] == 15 else a[0] + 1
    a[1] = 1 if a[1] == 28 else a[1] + 1
    a[2] = 1 if a[2] == 19 else a[2] + 1
    ans += 1
print(ans)