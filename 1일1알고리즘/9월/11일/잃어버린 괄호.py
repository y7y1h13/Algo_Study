import sys

input = sys.stdin.readline().strip
a = list(input())
Flag = False
tmp, ans = '', 0
for i in a:
    if Flag:
        if i == '+' or i == '-':
            ans -= int(tmp)
            tmp = ''
        else:
            tmp += i
    elif i == '-':
        Flag = True
        ans += int(tmp)
        tmp = ''
    elif i == '+':
        ans += int(tmp)
        tmp = ''
    else:
        tmp += i
if Flag:
    ans -= int(tmp)
else:
    ans += int(tmp)
print(ans)