a = list(input())
ans = 0
s = list()
for i in range(len(a)):
    if a[i] == '(':
        s.append('(')
    else:
        s.pop()
        if a[i - 1] == '(':
            ans += len(s)
        else:
            ans += 1
print(ans)