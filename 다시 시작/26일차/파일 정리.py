import sys
from collections import defaultdict

input = sys.stdin.readline
dic = defaultdict(int)
for _ in range(int(input())):
    name, extension = input().strip().split('.')
    dic[extension] += 1
for key, value in dict(sorted(dic.items())).items():
    print(key, value)
