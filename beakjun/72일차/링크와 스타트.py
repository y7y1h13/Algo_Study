def re(num, n):
    global ans
    if num == N // 2:
        link = list(set(people) - (set(start)))
        tmp = abs(score(start) - score(link))
        if ans > tmp:
            ans = tmp
        return
    for i in range(n, N):
        start.append(i)
        re(num+1, i+1)
        start.pop()


def score(team):
    sc = 0
    for i in team:
        for j in team:
            sc += a[i-1][j-1]
    return sc


N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
people = [i for i in range(N)]
ans = 1000000
start = []
re(0, 0)
print(ans)