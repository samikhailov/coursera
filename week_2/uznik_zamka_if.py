kirp = [int(input()), int(input()), int(input())]
otv = [int(input()), int(input())]
kirp.sort()
otv.sort()
if otv[0] >= kirp[0] and otv[1] >= kirp[1]:
    print('YES')
else:
    print('NO')
