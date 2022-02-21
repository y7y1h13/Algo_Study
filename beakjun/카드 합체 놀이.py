a, b = map(int, input().split())
k = list(map(int, input().split()))
for i in range(b):
    k.sort()
    k[0] = k[1] = k[0] + k[1]

print(sum(i for i in k))