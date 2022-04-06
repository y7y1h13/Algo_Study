a = list(input())
ans = []
while a:
    ans.append(''.join(a))
    a.pop(0)
ans.sort()
while ans:
    print(ans.pop(0))