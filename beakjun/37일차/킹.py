a, b, N = input().split()
m = [input() for _ in range(int(N))]
a = list(a)
b = list(b)

for i in range(2):
    if a[i] == 'A':
        a[i] = 1