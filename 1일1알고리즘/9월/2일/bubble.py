a = [2, 1, 5, 4, 3]

for i in range(1, len(a)):
    k = i
    while k > 0 and a[k - 1] > a[k]:
        a[k - 1], a[k] = a[k], a[k - 1]
        k -= 1
print(a)