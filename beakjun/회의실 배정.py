a = [list(map(int, input().split())) for _ in range(int(input()))]
f = sorted(a, key=lambda x: (x[1], x[0]))
s = e = cnt = 0
for i in f:
    s = i[0]
    if cnt == 0:
        e = i[1]
        cnt += 1
    elif e <= s:
        cnt += 1
        e = i[1]
print(cnt)