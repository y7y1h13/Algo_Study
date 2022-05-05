a = input()
b = []
for x in a:
    b.append(a.count(x))
if b.count(max(b)) > 1:
    print('?')
else:
    print(a[b.index(max(b))])
