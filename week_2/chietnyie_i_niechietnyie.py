A = int(input())
B = int(input())
C = int(input())
if ((A % 2 == 0 or B % 2 == 0 or C % 2 == 0) and
        ((A + 1) % 2 == 0 or (B + 1) % 2 == 0 or (C + 1) % 2 == 0)):
    print('YES')
else:
    print('NO')
