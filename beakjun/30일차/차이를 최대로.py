from itertools import permutations
N = int(input())
a = sorted(list(map(int, input().split())))

case = list(permutations(a))

ans = 0
for i in case:
    tmp = 0
    for j in range(N - 1):
        tmp += abs(i[j] - i[j + 1])
    ans = max(tmp, ans)

print(ans)
