import math
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x2 < x1:
        x1, x2 = x2, x1
    print(x1, x2)
elif d == 0:
    x = (-b + math.sqrt(d)) / (2 * a)
    print(x)
