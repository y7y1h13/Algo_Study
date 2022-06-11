for r in range(int(input())):
    sub = {}
    round = 0
    N = int(input())
    for i in range(N):
        a = list(map(int, input().split()))
        sub[i + 1] = a[1:]

    while True:
        flag = True
        learn = []
        for i in range(N):
            if not len(sub[i + 1]):
                learn.append(i + 1)
                sub.pop(i)

        for i in sub:
            for j in learn:
                if j in sub[i]:
                    sub[i].remove(j)

        if flag:
            break
        round += 1


    print(f'#{r + 1} {round}')
