def selection_sort(a):
    for i in range(len(a)):
        m = i
        for j in range(i + 1, len(a)):
            if a[m] > a[j]:
                m = j
        if a[i] > a[m]:
            a[i], a[m] = a[m], a[i]

    return a


print(selection_sort([1, 4, 2, 3]))
