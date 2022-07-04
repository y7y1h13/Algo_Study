def bi_sec(l, r):
    global n
    global ans
    while l <= r:
        mid = (l + r) // 2
        if mid * (mid + 1) // 2 <= n:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1


if __name__ == "__main__":
    n = int(input())
    ans = 0
    bi_sec(1, n)
    print(ans)