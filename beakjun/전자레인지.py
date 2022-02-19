n = int(input())
ans = []
for i in (300, 60, 10):
    if n % 10 != 0:
        ans.append(-1)
        break
    ans.append(n//i)
    n %= i
print(*ans)