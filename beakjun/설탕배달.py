sugar = int(input())
an, sugar = divmod(sugar, 5)
an += (sugar // 3)
sugar = sugar % 3
if sugar != 0:
    print(-1)
else:
    print(an)