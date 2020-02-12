n = int(input())

if n % 10 in [5, 6, 7, 8, 9, 0] or n > 10 and n < 20:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
elif n % 10 in [2, 3, 4]:
    print(n, 'korovy')
