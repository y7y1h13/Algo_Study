def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]

    left = [i for i in a[1:] if pivot > i]
    right = [i for i in a[1:] if pivot <= i]

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([4, 1, 2, 3]))
