import random


def bi_sec(data, search):
    print(data)
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False
    mid = len(data) // 2
    if search == data[mid]:
        return True
    else:
        if search > data[mid]:
            return bi_sec(data[mid + 1:], search)
        else:
            return bi_sec(data[:mid], search)


data_list = random.sample(range(100), 10)
data_list.sort()
print(bi_sec(data_list, 3))