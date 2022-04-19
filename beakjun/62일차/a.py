from itertools import combinations

a = list(int(input())for _ in range(9))
for i in combinations(a, 7):
    if sum(i) == 100:
        print(*sorted(i), sep='\n')
        break