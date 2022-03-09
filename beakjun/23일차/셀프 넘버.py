def solution():
    n = set(range(1, 10001))
    rmv = set()
    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        rmv.add(i)
    n = n - rmv
    for k in sorted(n):
        print(k)


if __name__ == "__main__":
    solution()
