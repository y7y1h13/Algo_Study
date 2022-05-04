def dfs(depth, total):
    global Max
    global Min
    if depth == N:
        if Max < total:
            Max = total

        if Min > total:
            Min = total
        return

    for i in range(4):
        if i == 0 and op[i]:
            op[i] -= 1
            dfs(depth + 1, total + a[depth])
            op[i] += 1
        elif i == 1 and op[i]:
            op[i] -= 1
            dfs(depth + 1, total - a[depth])
            op[i] += 1
        elif i == 2 and op[i]:
            op[i] -= 1
            dfs(depth + 1, total * a[depth])
            op[i] += 1
        elif i == 3 and op[i]:
            op[i] -= 1
            if total >= 0:
                dfs(depth + 1, total // a[depth])
            else:
                dfs(depth + 1, -(-total // a[depth]))
            op[i] += 1


N = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
Max = -1e10
Min = 1e10
dfs(1, a[0])
print(Max)
print(Min)