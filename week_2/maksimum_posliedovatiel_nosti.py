max = -1
current = max
while current != 0:
    current = int(input())
    if current > max:
        max = current
print(max)
