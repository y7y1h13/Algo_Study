from collections import defaultdict


for _ in range(int(input())):
    n = int(input())
    a = defaultdict(int)
    ans = 1
    for _ in range(n):
        name, op = input().split()
        a[op] += 1
    for i in a:
        ans *= (a[i] + 1)
    print(ans - 1)