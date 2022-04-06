a = list(input())
stack = []

while a:
    i = a.pop()
    if i.isalpha():
        if (i.isupper() and ord(i) + 13 > 90) or i.islower() and ord(i) + 13 > 122:
            stack.append(chr(ord(i) - 13))
        else:
            stack.append(chr(ord(i) + 13))
    else:
        stack.append(i)
print(*reversed(stack), sep='')