a = [False, False] + [True] * 1000000
for i in range(2, 1001):
    if a[i]:
        for j in range(2*i, 1000001, i):
            a[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, len(a)):
        if a[i] and a[n-i]:
            print(f'{n} = {i} + {n-i}')
            break