import math
import sys
val = [None, None, None]
val[0] = int(input())
val[1] = int(input())
val[2] = int(input())
val.sort()
if val[0] + val[1] <= val[2]:
    print('impossible')
else:
    gamma = math.degrees(
        math.acos(
            (val[0] ** 2 + val[1] ** 2 - val[2] ** 2) / (2 * val[0] * val[1])
            )
        )
    if gamma == 90:
        print('rectangular')
    elif gamma < 90:
        print('acute')
    elif gamma > 90:
        print('obtuse')
