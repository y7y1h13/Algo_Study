def bubble_sort(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return a


print(bubble_sort([8, 4, 2, 3]))
