def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    l, r = 0, 0
    a = list()
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            a.append(left[l])
            l += 1
        else:
            a.append(right[r])
            r += 1
    a += left[l:]
    a += right[r:]
    return a



print(merge_sort([6, 5, 3, 1, 8, 7, 2, 4]))
