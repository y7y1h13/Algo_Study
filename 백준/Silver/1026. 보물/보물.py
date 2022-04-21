n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
tot = 0
for i in a:
    tot += max(b) * i
    b.remove(max(b))
print(tot)