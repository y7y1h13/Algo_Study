from sys import stdin

n = int(stdin.readline().strip())
a = list(int(stdin.readline().strip()) for _ in range(n))
stack, ans, cnt, flag = [], [], 1, False
for i in a:
    while cnt <= i:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    if stack[-1] == i:
        stack.pop()
        ans.append('-')
    else:
        flag = True
if flag:
    print('NO')
else:
    print(*ans, sep='\n')
