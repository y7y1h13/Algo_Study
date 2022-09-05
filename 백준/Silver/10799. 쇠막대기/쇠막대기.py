a = list(input())
stack = []
ans = 0

for i in range(len(a)):
    if a[i] == '(':
        stack.append(1)

    else:
        stack.pop()
        if a[i-1] == '(':
            ans += len(stack)
        else:
            ans += 1
print(ans)