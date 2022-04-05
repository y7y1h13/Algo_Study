N = int(input())
a = input()
num_list = [int(input()) for _ in range(N)]
stack = []
for i in a:
    if 'A' <= i <= 'Z':
        stack.append(num_list[ord(i) - ord('A')])

    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if i == '+':
            stack.append(n1 + n2)
        elif i == '-':
            stack.append(n1 - n2)
        elif i == '*':
            stack.append(n1 * n2)
        elif i == '/':
            stack.append(n1 / n2)
print('%.2f' % stack[0])
