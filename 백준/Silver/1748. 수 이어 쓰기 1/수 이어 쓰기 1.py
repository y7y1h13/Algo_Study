from sys import stdin

N = int(stdin.readline())
l = len(str(N))
ans = 0

for i in range(l - 1):
    ans += 9 * 10 ** i * (i+1)
print(ans + (N - 10 ** (l-1) + 1) * l)
