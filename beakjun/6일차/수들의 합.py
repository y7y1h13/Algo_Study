n = int(input())
i = 1
cnt = 1
while True:
    n -= i
    if n <= i:
        print(cnt)
        break
    else:
        cnt += 1
        i += 1
