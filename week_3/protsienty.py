import math
p, x, y = float(input()), int(input()), int(input())
result = math.modf((x * 100 + y) * (p + 100) / 10000)
print(int(result[1]), int((result[0] + 10 ** (-9)) * 100))
