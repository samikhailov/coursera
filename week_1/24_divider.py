a = int(input())
b = int(input())
print((a % b) // (a % b or 1) * 'NO' or 'YES')
