n = int(input())

print('+___ ' * n)
print(*[f'|{i} /' for i in range(1, n + 1)])
print('|__\ ' * n)
print('|    ' * n)
