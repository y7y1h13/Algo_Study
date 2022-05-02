from itertools import combinations


while True:
    a = list(map(int, input().split()))
    if 0 in a:
        break
    for i in combinations(a[1:], 6):
        print(*i)
    print()
