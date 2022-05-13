import math

n = int(input())
prime_number = []
array = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2

        while i * j <= n:
            array[i * j] = False
            j += 1

for num in range(2, n + 1):
    if array[num]:
        prime_number.append(num)
print(prime_number)