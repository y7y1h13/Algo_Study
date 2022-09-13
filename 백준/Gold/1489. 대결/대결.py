n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
score = 0

for i in range(n):
    for j in range(n):
        if a[i] > b[j] != 0:
            score += 2
            a[i] = 0
            b[j] = 0
            break


for i in range(n):
    if a[i] == 0:
        continue
    for j in range(n):
        if a[i] == b[j] != 0:
            score += 1
            b[j] = 0
            break

print(score)
