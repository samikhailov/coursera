a = int(input())
b = int(input())
if b % (b - a + 1) == 0:
    print('YES')
else:
    print('NO')
