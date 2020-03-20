from functools import reduce

print(reduce(lambda x, y: x * y, list(map(int, input().split()))) ** 5)
