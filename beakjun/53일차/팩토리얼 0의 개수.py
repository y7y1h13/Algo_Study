n = int(input())
ans, cnt = 1, 0
while n > 0:
    ans *= n
    n -= 1
for i in list(reversed(str(ans))):
    if i == '0':
        cnt += 1
    elif i != '0':
        break
print(cnt)
# t=int(input())//5
# print(t+t//5+t//25)