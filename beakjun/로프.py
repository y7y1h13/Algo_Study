a = list(int(input()) for _ in range(int(input())))
tmp = 0
for idx, k in enumerate(sorted(a, reverse=True)):
    if tmp < k * (idx+1):
        tmp = k * (idx+1)
print(tmp)
