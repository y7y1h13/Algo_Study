while True:
    try:
        a = input().rstrip('\n')
        if not a:
            break
        ans = [0] * 4
        for i in a:
            ans[0] += 1 if i.islower() else 0
            ans[1] += 1 if i.isupper() else 0
            ans[2] += 1 if i.isdigit() else 0
            ans[3] += 1 if i.isspace() else 0
        print(*ans)
    except EOFError:
        break
        