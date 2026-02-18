number = int(input())
table = [-1] * (number + 1)

if number >= 0:
    table[0] = 0
if number >= 1:
    table[1] = 1

def dp(n: int):
    if table[n] != -1:
        return table[n]
    table[n] = dp(n-1) + dp(n-2)
    return table[n]

print(dp(number))
