from math import gcd
from itertools import combinations


for i in range(int(input())):
    ans = 0
    a = list(map(int, input().split()))
    for j in combinations(a[1:], 2):
        ans += gcd(j[0], j[1])
    print(ans)
