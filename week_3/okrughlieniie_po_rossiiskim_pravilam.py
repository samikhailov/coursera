import math
n = float(input())
parts = math.modf(n)
if parts[0] >= 0.5:
    print(int(parts[1] + 1))
else:
    print(int(parts[1]))
