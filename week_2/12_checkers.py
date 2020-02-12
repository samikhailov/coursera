x = int(input())
y = int(input())
x2 = int(input())
y2 = int(input())
if (x - y) % 2 == 0 and (x2 - y2) % 2 == 0 and y < y2 and y2 - y >= x2 - x:
    print('YES')
else:
    print('NO')
