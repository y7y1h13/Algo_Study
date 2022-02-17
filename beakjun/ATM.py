p = int(input())
t = sorted(list(map(int, input().split())))
s = tmp = 0
for i in t:
    tmp += i
    s += tmp
print(s)
