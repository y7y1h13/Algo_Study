def fact(N):
    if N > 1: 
        return N * fact(N - 1)
    else:
        return 1
print(fact(int(input())))