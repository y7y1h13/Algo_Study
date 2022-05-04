def dfs(depth, total):
    global Max
    global Min
    if depth == N:
        if Max < total:
            Max = total

        if Min > total:
            Min = total
        return
    if op[0] > 0:
        op[0] -= 1
        dfs(depth + 1, total + a[depth])
        op[0] += 1

    if op[1] > 0:
        op[1] -= 1
        dfs(depth + 1, total - a[depth])
        op[1] += 1

    if op[2] > 0:
        op[2] -= 1
        dfs(depth + 1, total * a[depth])
        op[2] += 1

    if op[3] > 0:
        op[3] -= 1
        dfs(depth + 1, int(total / a[depth]))
        op[3] += 1
N = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
Max = -1e10
Min = 1e10
dfs(1, a[0])
print(Max)
print(Min)