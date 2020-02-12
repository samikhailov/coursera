a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (abs(a1-b1) - abs(a2-b2)) % 2 == 0:
    print('YES')
else:
    print('NO')
