import math
num = f'{int(input()):04d}'
num1 = int(num[:2])
num2 = int(num[3] + num[2])
if num1 == num2:
    print(1)
else:
    print(0)
