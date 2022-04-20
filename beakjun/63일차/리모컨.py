N, M = int(input()), int(input())
if M > 0:
    a = list(map(int, input().split()))
else:
    a = list()
ans = abs(100 - N)

for i in range(1000000):
    n = str(i)
    for j in range(len(n)):
        if int(n[j]) in a:
            break
        elif j == len(n) - 1:
            ans = min(abs(int(n) - N) + len(n), ans)
print(ans)