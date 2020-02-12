num = int(input())
print(f'{num // 3600 % 24}:{num // 60 % 60:02d}:{num % 60:02d}')
