T = int(input())

for _ in range(T):
    t = int(input())
    n0 = [1, 0]
    n1 = [0, 1]
    if t > 1:
        for i in range(2, t + 1):
            n0.append(n0[i - 1] + n0[i - 2])
            n1.append(n1[i - 1] + n1[i - 2])
    print(n0[t], n1[t])
