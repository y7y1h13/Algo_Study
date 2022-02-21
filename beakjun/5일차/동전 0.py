n, m = map(int, input().split())
cnt = 0
for i in sorted(list(int(input()) for _ in range(n)), reverse=True):
    if i <= m:
        cnt += (m // i)
        m %= i
print(cnt)
