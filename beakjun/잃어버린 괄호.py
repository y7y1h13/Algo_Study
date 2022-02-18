n = input().split('-')
s = 0
for i in n[0].split('+'):
    s += int(i)
for i in n[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
