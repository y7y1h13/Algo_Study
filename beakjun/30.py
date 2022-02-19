n = sorted(map(int, list(input())), reverse=True)
if (0 not in n) or (sum(i for i in n) % 3 != 0):
    print(-1)
else:
    print(int(''.join(map(str, n))))
