l = [int(i) for i in input().split()]
m = set()

for i in l:
    if i in m:
        print('YES')
    else:
        print('NO')
    m.add(i)
