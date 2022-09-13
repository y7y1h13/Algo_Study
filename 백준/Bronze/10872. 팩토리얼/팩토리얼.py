def fact(N):
    return N * fact(N - 1) if N > 1 else 1
print(fact(int(input())))