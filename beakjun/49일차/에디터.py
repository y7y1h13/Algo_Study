from sys import stdin


stack1 = list(map(str, stdin.readline().strip()))
stack2 = []

for _ in range(int(stdin.readline().strip())):
    a = list(stdin.readline().strip().split())
    if a[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())

    elif a[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())

    elif a[0] == 'B':
        if stack1:
            stack1.pop()

    else:
        stack1.append(a[1])
stack1.extend(reversed(stack2))
print(''.join(stack1))