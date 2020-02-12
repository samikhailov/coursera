a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if d > e:
    d, e = e, d
if c <= e and b <= d:
    print('YES')
else:
    print('NO')
