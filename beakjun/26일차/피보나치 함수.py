def fibo_dp(n, a, b):

    if n == 0:
        a += 1
        return 0
    elif n == 1:
        b += 1
        return 1
    else:
        print(a, b)
        return fibo_dp(n - 1) + fibo_dp(n - 2)

a = 0
b = 0
print(fibo_dp(int(input()),a,b))
