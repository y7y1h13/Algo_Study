p = input()
s = tmp = 0
for i in sorted(map(int, input().split())):
    tmp += i
    s += tmp
print(s)